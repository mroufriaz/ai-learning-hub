from django.shortcuts import render, get_object_or_404
from .models import Course

def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    # Fetch course
    course = get_object_or_404(Course, id=course_id)

    # Fetch related courses (same category, excluding current one)
    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)[:5]

    context = {
        'course': course,  
        'related_courses': related_courses
    }
    return render(request, 'courses/course_detail.html', context)
