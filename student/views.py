from .utils import dictionary_extractors

from django.shortcuts import render
from django.http import HttpResponse
from .models.student import Student
from .models.exams import Exam
from .models.pay import Pay
from .forms import BasicForm, ExamForm, PayForm


def full_info(request):
    students = Student.objects.all()
    context = {'students': students}

    return render(request, 'landing/full.html', context)


def basic_info(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'landing/basic.html', context)


def exam_info(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'landing/exam.html', context)


def financial_info(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'landing/financial.html', context)


def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        basic_form = BasicForm(request.POST)
        if basic_form.is_valid():
            return HttpResponse(request.POST['first_name'])
    else:
        # prepare the basic form
        basic_form_context = dictionary_extractors.basic_form(student)
        basic_form = BasicForm(basic_form_context)
        # prepare the exam forms
        exam_forms = []
        exams = Exam.objects.filter(student__id=student.id)
        form_number = 'A'
        # fill with bound data
        for exam in exams:
            exam_form_context = dictionary_extractors.exam_form(exam)
            exam_form = ExamForm(exam_form_context)
            exam_form.form_number = form_number
            form_number = 'B'
            exam_forms.append(exam_form)
        # empty forms
        exam_forms_number = len(exam_forms)
        if exam_forms_number < 2:
            for i in range(2 - exam_forms_number):
                empty_form = ExamForm()
                empty_form.form_number = form_number
                exam_forms.append(empty_form)
                form_number = 'B'
        # prepare the pay forms
        pay_forms = []
        pays = Pay.objects.filter(student__id=student.id)
        form_number = 1
        # fill with bound data
        for pay in pays:
            pay_form_context = dictionary_extractors.pay_form(pay)
            pay_form = PayForm(pay_form_context)
            pay_form.form_number = form_number
            form_number += 1
            pay_forms.append(pay_form)
        # empty forms
        pay_form_number = len(pay_forms)
        if pay_form_number < 10:
            for i in range(10 - pay_form_number):
                empty_form = PayForm()
                empty_form.form_number = form_number
                pay_forms.append(empty_form)
                form_number += 1

    return render(request, 'forms/edit.html', {'basic_form': basic_form, 'exam_forms': exam_forms,
                                               'pay_forms': pay_forms})
