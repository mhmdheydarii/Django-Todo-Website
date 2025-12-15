from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return self.title