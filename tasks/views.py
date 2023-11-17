from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi

class TaskList(APIView):

    @swagger_auto_schema(
        operation_description="Get a list of tasks",
        responses={200: openapi.Response('List of tasks', TaskSerializer(many=True))}
    )
    def get(self, request, format=None):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new task",
        request_body=TaskSerializer,
        responses={201: 'Created', 400: 'Bad Request'}
    )

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get details of a specific task",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Task ID", type=openapi.TYPE_INTEGER),
        ],
        responses={200: openapi.Response('Task details', TaskSerializer)}
    )

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer =TaskSerializer(task)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update details of a specific task",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Task ID", type=openapi.TYPE_INTEGER),
        ],
        request_body=TaskSerializer,
        responses={200: 'Updated', 400: 'Bad Request'}
    )

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a specific task",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Task ID", type=openapi.TYPE_INTEGER),
        ],
        responses={204: 'No Content'}
    )

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):

    @swagger_auto_schema(
        operation_description="Get a list of category",
        responses={200: openapi.Response('List of category', CategorySerializer(many=True))}
    )

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new category",
        request_body=CategorySerializer,
        responses={201: 'Created', 400: 'Bad Request'}
    )

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get details of a specific category",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Category ID", type=openapi.TYPE_INTEGER),
        ],
        responses={200: openapi.Response('Category details', CategorySerializer)}
    )

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update details of a specific category",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Category ID", type=openapi.TYPE_INTEGER),
        ],
        request_body=CategorySerializer,
        responses={200: 'Updated', 400: 'Bad Request'}

    )

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a specific category",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Category ID", type=openapi.TYPE_INTEGER),
        ],
        responses={204: 'No Content'}
    )

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)