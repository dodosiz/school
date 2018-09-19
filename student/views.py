from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models.student import Student
from .forms import StudentForm


def full_info(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'full.html', context)


def basic_info(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'basic.html', context)


def exam_info(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'exam.html', context)


def financial_info(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'financial.html', context)


def detail(request, student_id):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('full_info')
    else:
        form = StudentForm()

    return render(request, 'detail.html', {'form': form})

