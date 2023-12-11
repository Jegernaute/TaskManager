from rest_framework import serializers
from tasks.models import Task, Category
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['category', 'title', 'description', 'deadline', 'priority', 'status_of_tasks', 'date_of_create']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name_of_category']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

    def validate_email(self, value):
        # Кастомна валідація для формату електронної пошти
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError('Електронна пошта повинна закінчуватися на @gmail.com.')
        return value

    def validate_password(self, value):
        # Кастомна валідація для паролю (наприклад, довжина паролю)
        if len(value) < 8:
            raise serializers.ValidationError('Пароль повинен бути не менше 8 символів.')
        return value

    def validate(self, data):
        # Перевірка, чи користувач з таким ім'ям вже існує
        username = data.get('email')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Користувач з таким іменем вже існує.')
        return data

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        user = User.objects.create_user(**validated_data)
        return user