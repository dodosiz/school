def basic_form(student):
    basic_form_context = dict()
    basic_form_context['first_name'] = student.first_name
    basic_form_context['last_name'] = student.last_name
    basic_form_context['fathers_name'] = student.family.fathers_name
    basic_form_context['mothers_name'] = student.family.mothers_name
    basic_form_context['fathers_job'] = student.family.fathers_job
    basic_form_context['mothers_job'] = student.family.mothers_job
    basic_form_context['afm'] = student.financial.afm
    basic_form_context['fees'] = student.financial.fees
    basic_form_context['telephone_1'] = student.contact.telephone_1
    basic_form_context['telephone_2'] = student.contact.telephone_2
    basic_form_context['address'] = student.contact.address

    return basic_form_context


def exam_form(exam):
    exam_form_context = dict()
    exam_form_context['dictionary'] = exam.dictionary
    exam_form_context['speaking'] = exam.speaking
    exam_form_context['listening'] = exam.listening
    exam_form_context['reading'] = exam.reading
    exam_form_context['writing'] = exam.writing
    exam_form_context['grammar'] = exam.grammar
    exam_form_context['test'] = exam.test
    exam_form_context['exams'] = exam.exams

    return exam_form_context


def pay_form(pay):
    pay_form_context = dict()
    pay_form_context['pay'] = pay.pay
    pay_form_context['date'] = pay.date
    pay_form_context['service_number'] = pay.service_number

    return pay_form_context

