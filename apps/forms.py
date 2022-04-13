from django.forms  import ModelForm
from .models import *


class Todo_Task_form(ModelForm):
    class Meta:
        model = TodoData
        fields = ['name_of_task',   'task', 'created_by',  'date_started', 'date_completed', 'done']
        exclude = ['date_completed', 'date_started']



