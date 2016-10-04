from django.shortcuts import render
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'tutorial/course_list.html', {'courses': courses})
