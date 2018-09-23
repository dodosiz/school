from .utils import dictionary_extractors

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models.student import Student
from .models.exams import Exam
from .models.pay import Pay
from .models.basics import FamilyInfo, FinancialInfo, ContactInfo
from .forms import BasicForm, ExamForm, PayForm


def full_info(request, success_message=''):
    students = Student.objects.all()
    context = {'students': students, 'success_message': success_message}

    return render(request, 'landing/full.html', context)


def basic_info(request, success_message=''):
    students = Student.objects.all()
    context = {'students': students, 'success_message': success_message}
    return render(request, 'landing/basic.html', context)


def exam_info(request, success_message=''):
    students = Student.objects.all()
    context = {'students': students, 'success_message': success_message}
    return render(request, 'landing/exam.html', context)


def financial_info(request, success_message=''):
    students = Student.objects.all()
    context = {'students': students, 'success_message': success_message}
    return render(request, 'landing/financial.html', context)


def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        # update student
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.save()
        # update family
        family = student.family
        family.fathers_name = request.POST['fathers_name']
        family.mothers_name = request.POST['mothers_name']
        family.fathers_job = request.POST['fathers_job']
        family.mothers_job = request.POST['mothers_job']
        family.save()
        # update financial info
        financial = student.financial
        if request.POST['afm']:
            financial.afm = request.POST['afm']
        if request.POST['fees']:
            financial.fees = request.POST['fees']
        financial.save()
        # update contact info
        contact = student.contact
        contact.telephone_1 = request.POST['telephone_1']
        contact.telephone_2 = request.POST['telephone_2']
        contact.address = request.POST['address']
        contact.save()
        # update exams
        for c in ['A', 'B']:
            # update exam
            if request.POST['exam_id_'+c]:
                exam = Exam.objects.get(id=request.POST['exam_id_'+c])
                exam.dictionary = request.POST['dictionary_'+c]
                exam.speaking = request.POST['speaking_' + c]
                exam.listening = request.POST['listening_' + c]
                exam.reading = request.POST['reading_' + c]
                exam.writing = request.POST['writing_' + c]
                exam.grammar = request.POST['grammar_' + c]
                exam.test = request.POST['test_' + c]
                exam.exams = request.POST['exams_' + c]
                exam.save()
            # create new
            elif request.POST['dictionary_'+c] or request.POST['speaking_' + c] or request.POST['listening_' + c]\
                    or request.POST['reading_' + c] or request.POST['writing_' + c] or request.POST['grammar_' + c]\
                    or request.POST['test_' + c] or request.POST['exams_' + c]:
                exam = Exam()
                exam.dictionary = request.POST['dictionary_' + c]
                exam.speaking = request.POST['speaking_' + c]
                exam.listening = request.POST['listening_' + c]
                exam.reading = request.POST['reading_' + c]
                exam.writing = request.POST['writing_' + c]
                exam.grammar = request.POST['grammar_' + c]
                exam.test = request.POST['test_' + c]
                exam.exams = request.POST['exams_' + c]
                exam.student = student
                exam.save()
        for i in range(1, 11):
            # update pay
            if request.POST['pay_id_'+str(i)]:
                pay = Pay.objects.get(id=request.POST['pay_id_'+str(i)])
                if request.POST['pay_' + str(i)]:
                    pay.pay = float(request.POST['pay_'+str(i)])
                else:
                    pay.pay = 0.0
                if request.POST['date_' + str(i)]:
                    pay.date = request.POST['date_' + str(i)]
                if request.POST['service_number_' + str(i)]:
                    pay.service_number = int(request.POST['service_number_' + str(i)])
                else:
                    pay.service_number = 0
                pay.save()
            # create new
            elif request.POST['pay_' + str(i)] or request.POST['date_' + str(i)]\
                    or request.POST['service_number_' + str(i)]:
                pay = Pay()
                if request.POST['pay_'+str(i)]:
                    pay.pay = float(request.POST['pay_' + str(i)])
                if request.POST['date_' + str(i)]:
                    pay.date = request.POST['date_' + str(i)]
                if request.POST['service_number_' + str(i)]:
                    pay.service_number = int(request.POST['service_number_' + str(i)])
                pay.student = student
                pay.save()
        request = HttpRequest()
        return full_info(request, 'Student updated successfully')
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
                                               'pay_forms': pay_forms, 'menu_message': 'Edit User'})


def new(request):
    if request.method == 'POST':
        # create student
        student = Student()
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        # create family
        family = FamilyInfo()
        family.fathers_name = request.POST['fathers_name']
        family.mothers_name = request.POST['mothers_name']
        family.fathers_job = request.POST['fathers_job']
        family.mothers_job = request.POST['mothers_job']
        family.save()
        # create financial info
        financial = FinancialInfo()
        if request.POST['afm']:
            financial.afm = request.POST['afm']
        if request.POST['fees']:
            financial.fees = request.POST['fees']
        financial.save()
        # create contact info
        contact = ContactInfo()
        contact.telephone_1 = request.POST['telephone_1']
        contact.telephone_2 = request.POST['telephone_2']
        contact.address = request.POST['address']
        contact.save()
        student.family = family
        student.financial = financial
        student.contact = contact
        student.save()
        for c in ['A', 'B']:
            # create exam
            if request.POST['dictionary_'+c] or request.POST['speaking_' + c] or request.POST['listening_' + c]\
                    or request.POST['reading_' + c] or request.POST['writing_' + c] or request.POST['grammar_' + c]\
                    or request.POST['test_' + c] or request.POST['exams_' + c]:
                exam = Exam()
                exam.dictionary = request.POST['dictionary_' + c]
                exam.speaking = request.POST['speaking_' + c]
                exam.listening = request.POST['listening_' + c]
                exam.reading = request.POST['reading_' + c]
                exam.writing = request.POST['writing_' + c]
                exam.grammar = request.POST['grammar_' + c]
                exam.test = request.POST['test_' + c]
                exam.exams = request.POST['exams_' + c]
                exam.student = student
                exam.save()
        for i in range(1, 11):
            # create pay
            if request.POST['pay_' + str(i)] or request.POST['date_' + str(i)]\
                    or request.POST['service_number_' + str(i)]:
                pay = Pay()
                if request.POST['pay_'+str(i)]:
                    pay.pay = float(request.POST['pay_' + str(i)])
                if request.POST['date_' + str(i)]:
                    pay.date = request.POST['date_' + str(i)]
                if request.POST['service_number_' + str(i)]:
                    pay.service_number = int(request.POST['service_number_' + str(i)])
                pay.student = student
                pay.save()
        request = HttpRequest()
        return full_info(request, 'Student created successfully')
    else:
        # prepare the basic form
        basic_form = BasicForm()
        # prepare the exam forms
        exam_forms = []
        form_number = 'A'
        for i in range(2):
            empty_form = ExamForm()
            empty_form.form_number = form_number
            exam_forms.append(empty_form)
            form_number = 'B'
        # prepare the pay forms
        pay_forms = []
        form_number = 1
        for i in range(10):
            empty_form = PayForm()
            empty_form.form_number = form_number
            pay_forms.append(empty_form)
            form_number += 1

    return render(request, 'forms/edit.html', {'basic_form': basic_form, 'exam_forms': exam_forms,
                                               'pay_forms': pay_forms, 'menu_message': 'New User'})
