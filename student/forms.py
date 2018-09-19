from django import forms


class StudentForm(forms.Form):
    # basic info
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fathers_name = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mothers_name = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fathers_job = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mothers_job = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    afm = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fees = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone_1 = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone_2 = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # exams a
    dictionary_a = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    speaking_a = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    listening_a = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    reading_a = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    writing_a = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    grammar_a = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    test_a = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exams_a = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # exams b
    dictionary_b = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    speaking_b = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    listening_b = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    reading_b = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    writing_b = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    grammar_b = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    test_b = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exams_b = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pay 1
    pay_1 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_1 = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
    service_number_1 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pay 2
    pay_2 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_2 = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
    service_number_2 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pay 3
    pay_3 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_3 = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
    service_number_3 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pay 4
    pay_4 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_4 = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
    service_number_4 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pay 5
    pay_5 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_5 = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
    service_number_5 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pay 6
    pay_6 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_6 = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
    service_number_6 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pay 7
    pay_7 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_7 = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
    service_number_7 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pay 8
    pay_8 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_8 = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
    service_number_8 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pay 9
    pay_9 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_9 = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
    service_number_9 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # pay 10
    pay_10 = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_10 = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
    service_number_10 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))