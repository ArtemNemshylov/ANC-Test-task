from django.shortcuts import render


def homepage(request):
    return render(request, 'tree/base.html')


def show_tree(request):
    return render(request, 'tree/home.html')


def populate_db(request):
    return render(request, 'tree/populate_db.html')