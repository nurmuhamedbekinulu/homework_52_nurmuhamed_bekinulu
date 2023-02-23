from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task
from django.http import HttpResponseNotFound
from django.urls import reverse
from static.classes.static import Static


def add_view(request: WSGIRequest):
    if request.method == "GET":
        choices = Static.choices
        return render(request, 'task_create.html', context={'choices': choices})
    
    if request.POST.get('completion_date') != "":
        completion_date = request.POST.get('completion_date')
    else:
        completion_date = None

    task_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'completion_date': completion_date
    }
    task = Task.objects.create(**task_data)
    return redirect('task_detail', pk=task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
        })