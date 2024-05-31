from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .scripts import database_seeder
from .models import Employee


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
    # Получаем сотрудников первого уровня и их подчиненных
    level_1_employees = Employee.objects.filter(level=1).prefetch_related('subordinates')

    context = {
        'level_1_employees': level_1_employees,
    }
    return render(request, 'tree/hierarchy.html', context)
