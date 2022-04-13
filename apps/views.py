from asyncio import all_tasks
from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from .models import TodoData
from django.http import HttpResponseRedirect
from .forms import *
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
    if request.method == 'POST':
        forms = Todo_Task_form(request.POST)
        if forms.is_valid():    
            new_todo = forms.save(commit=False)
            new_todo.save()
            return redirect("listtask")
        else:
            forms = Todo_Task_form()
    else:
        forms = Todo_Task_form()
        
    return render(request, 'create.html', {'forms': forms})

# delete
def  DeleteTask(request, pk):
    tod_task = TodoData.objects.all().filter(pk=pk)
    tod_task.delete()
    return redirect('/')


# update
def  UpdateTask(request, pk):
    todoapp_in_question = TodoData.objects.get(pk = pk)
    formUpdate = Todo_Task_form(request.POST, instance=todoapp_in_question)

    
    if request.method == "POST":
        if formUpdate.is_valid():
            formUpdate.save()
            return redirect("home")
        else:
            
            return render(request, "update.html", {formUpdate: "formUpdate"})
    return render(request, "update.html", {"formUpdate": formUpdate})
   