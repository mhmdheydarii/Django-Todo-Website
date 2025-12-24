from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=250)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return self.task