from django.contrib import admin
from django.urls import path

# import needed to register the model
from apps import views
from apps.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ListTask, name='listtask'), # list all tasks
    path('create', views.CreateTask, name='createtask'),
    path('delete\<int:pk>', views.DeleteTask, name='deletetask'),
    path('update\<int:pk>', views.UpdateTask, name='updatetask'),
]
