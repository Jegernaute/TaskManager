from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import register_user

urlpatterns = [
    path('task/', views.TaskList.as_view()),
    path('task/<int:pk>/', views.TaskDetail.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('drf-auth/', include('rest_framework.urls')),
    path('register/', register_user, name='register_user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)