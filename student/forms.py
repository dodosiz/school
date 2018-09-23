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
    element_id = forms.IntegerField(required=False)
    dictionary = forms.CharField(max_length=50, required=False,
                                   widget=forms.TextInput())
    speaking = forms.CharField(max_length=50, required=False, widget=forms.TextInput())
    listening = forms.CharField(max_length=50, required=False,
                                  widget=forms.TextInput())
    reading = forms.CharField(max_length=50, required=False, widget=forms.TextInput())
    writing = forms.CharField(max_length=50, required=False, widget=forms.TextInput())
    grammar = forms.CharField(max_length=50, required=False, widget=forms.TextInput())
    test = forms.CharField(max_length=50, required=False, widget=forms.TextInput())
    exams = forms.CharField(max_length=50, required=False, widget=forms.TextInput())


class PayForm(forms.Form):
    form_number = 0
    element_id = forms.IntegerField(required=False)
    pay = forms.FloatField(required=False)
    date = forms.DateField(required=False)
    service_number = forms.IntegerField(required=False)
