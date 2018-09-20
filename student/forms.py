from django import forms


class BasicForm(forms.Form):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fathers_name = forms.CharField(max_length=255, required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    mothers_name = forms.CharField(max_length=255, required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    fathers_job = forms.CharField(max_length=255, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    mothers_job = forms.CharField(max_length=255, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    afm = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fees = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone_1 = forms.CharField(max_length=100, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone_2 = forms.CharField(max_length=100, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ExamForm(forms.Form):
    form_number = ''
    dictionary = forms.CharField(max_length=50, required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    speaking = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    listening = forms.CharField(max_length=50, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    reading = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    writing = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    grammar = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    test = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exams = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


class PayForm(forms.Form):
    form_number = 0
    pay = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
    service_number = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))