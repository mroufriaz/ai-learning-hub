from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('course_detail/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses_sidebar/', views.courses_sidebar, name='courses_sidebar'),
]
