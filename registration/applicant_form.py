from django import forms

from .models import applicant_model

gender=[('M','Male'),('F','Female'),('T','Transgender')]
class DateInput(forms.DateInput):
    input_type='date'
class applicant_form(forms.ModelForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)





    class Meta:
        model= applicant_model
        fields=('id','applicant_name','address','mobile','email')