from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tree.scripts import database_seeder
from .models import Employee
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from .forms import EmployeeForm
import logging


def homepage_view(request):
    return render(request, 'tree/base.html')


def show_tree_view(request):
    return render(request, 'tree/home.html')


@csrf_exempt
def populate_db_view(request):
    if request.method == 'POST':
        database_seeder.first_seed()
        return JsonResponse({'status': 'success'}, status=200)

    employee_count = Employee.objects.count()
    return render(request, 'tree/populate_db.html', {'employee_count': employee_count})


def progress_view(request):
    current_count = Employee.objects.count()
    total_count = 88572  # Общее количество сотрудников, которое будет добавлено
    return JsonResponse({'current_count': current_count, 'total_count': total_count})


def show_hierarchy(request):
    # Получаем только объекты Employee первого уровня
    level_1_employees = Employee.objects.filter(level=1)
    context = {
        'level_1_employees': level_1_employees,
    }
    return render(request, 'tree/hierarchy.html', context)


def get_subordinates(request, employee_id):
    subordinates = Employee.objects.filter(chief_id=employee_id).values('id', 'full_name', 'position')
    return JsonResponse(list(subordinates), safe=False)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('show_hierarchy')
    else:
        form = RegisterForm()
    return render(request, 'tree/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user.check_password(password):
                    login(request, user)
                    return redirect('show_hierarchy')
    else:
        form = LoginForm()
    return render(request, 'tree/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('show_hierarchy')


logger = logging.getLogger(__name__)


def employee_list(request):
    sort = request.GET.get('sort', 'full_name')
    direction = request.GET.get('direction', 'asc')

    if direction == 'desc':
        sort = '-' + sort

    employees = Employee.objects.all().order_by(sort)

    context = {
        'employees': employees,
        'current_sort': sort.lstrip('-'),
        'sort_direction': 'desc' if direction == 'asc' else 'asc'
    }
    return render(request, 'tree/employee_list.html', context)


def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'tree/employee_edit.html', {'form': form})


def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'tree/employee_add.html', {'form': form})
