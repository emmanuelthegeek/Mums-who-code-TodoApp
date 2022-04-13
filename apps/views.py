from asyncio import all_tasks
from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from .models import TodoData
from django.http import HttpResponseRedirect

# Create your views here.
#CRUD CREATE, READ, UPDATE, DELETE
# read
def  ListTask(request):
    context = {}
    all_tasks = TodoData.objects.all()
    context['all_tasks'] = all_tasks
    return render(request, 'homepage.html', context)

# create
def  CreateTask(request):
    name_of_task =request.POST['name_of_task']
    TodoData.objects.create(name_of_task=name_of_task)
    return render(request, 'create.html')

# delete
def  DeleteTask(request, pk):
    tod_task = TodoData.objects.all().filter(pk=pk)
    tod_task.delete()
    return redirect('/')


# update
def  UpdateTask(request, pk):
    TodoData = get_object_or_404(TodoData, pk=id)
    isdone = request.POST.get('isdone', False)
    if isdone == 'on':
        isdone == True
    TodoData.isdone = isdone

    TodoData.save()
    return render(request, 'update.html')