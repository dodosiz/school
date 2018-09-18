from django.shortcuts import render
from .models.student import Student


def students_view(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'index.html', context)
