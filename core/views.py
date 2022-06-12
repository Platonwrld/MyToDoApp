from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User

def index(request):

    user = request.user

    if user.is_authenticated:
        tasks = Task.objects.all()

        user_id = request.user.id

        context = {
            'tasks': tasks,
            'user_id': user_id,
            }

        return render(request, 'index.html', context=context)

    else:
        return render(request, 'main_page.html', {})


def delete_task(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {
        'task': task,
    }

    return render(request, 'delete_task.html', context=context)


def update_task(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = TaskForm(instance=task)

    context = {
        'task': task,
        'form': form,
    }

    return render(request, 'update_task.html', context=context)


def create_task(request):

    form = TaskForm(request.POST or None)

    if request.method == 'POST':


        if form.is_valid():                     

            print("\n\n its valid")

            author = Author.objects.get(user=request.user)  

            new_task = form.save(commit=False)   
            new_task.user = author
            new_task.save()

            form.save_m2m()

            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'create_task.html', context=context)