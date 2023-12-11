from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name_of_category = models.CharField(max_length=255)

    def __str__(self):
        return self.name_of_category

class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField()
    status_of_tasks = models.CharField(max_length=255)
    date_of_create = models.DateTimeField(auto_now_add=True) # Владислав топ


