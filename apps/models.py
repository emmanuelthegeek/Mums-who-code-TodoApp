from django.db import models
# import user model
# first option for importing user model
from django.contrib.auth.models import User

# second option for importing user model

from django.contrib.auth import get_user_model

task_owner = get_user_model()


# Create your models here.
class TodoData(models.Model):
    name_of_task = models.CharField(max_length=100)
    task  =  models.TextField()
    date_started = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name_of_task
    
    # plural of the model name
    class Meta:
        verbose_name_plural = 'Todo Data'