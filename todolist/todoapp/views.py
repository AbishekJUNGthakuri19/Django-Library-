from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')


    return render(request, 'list.html', {'tasks':tasks , 'form':form})

def updateTask(request, pk):
    pk = int(pk)
    task = Task.objects.get(id=pk)


    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST or None ,instance=task)

        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'update_task.html', {'form':form})


# def deleteTask(request,pk):
#     pk = int(pk)
#     item = Task.objects.get(id=pk)

#     if request.method == 'POST':
#         item.delete()
#         return redirect('/')

#     return render(request,'delete.html',{'item':item})