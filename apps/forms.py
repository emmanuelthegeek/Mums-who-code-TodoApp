# forms.py
from django.forms  import ModelForm
from .models import *


class Todo_Task_form(ModelForm):
    class Meta:
        model = TodoData
        fields = ['name_of_task',   'task', 'created_by',  'done']
        exclude = ['date_completed', 'date_started']




