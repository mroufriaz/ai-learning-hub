from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Course



def courses(request):
    courses = Course.objects.all().order_by('-created_at')  

    # Set how many courses per page
    paginator = Paginator(courses, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'courses': page_obj.object_list,  
    }
    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    # Fetch the main course
    course = get_object_or_404(Course, id=course_id)

    # Related courses (same category, excluding current one)
    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)[:5]

    context = {
        'course': course,
        'related_courses': related_courses
    }
    return render(request, 'courses/course_detail.html', context)

def courses_sidebar(request):
    return render(request, 'courses/courses_sidebar.html')