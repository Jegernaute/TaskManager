from rest_framework import serializers
from tasks.models import Task, Category


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['category', 'title', 'description', 'deadline', 'priority', 'status_of_tasks', 'date_of_create']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name_of_category']