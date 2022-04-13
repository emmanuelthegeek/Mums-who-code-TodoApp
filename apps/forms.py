from django.forms  import ModelForm
from .models import *


class Todo_Task_form(ModelForm):
    class Meta:
        model = TodoData
        fields = ['name_of_task', 'date_started', 'date_completed', 'isdone']
        exclude = ['date_completed']



