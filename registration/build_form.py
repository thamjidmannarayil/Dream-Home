from django import forms

from .models import builder_model

gender=[('M','Male'),('F','Female'),('T','Transgender')]
class DateInput(forms.DateInput):
    input_type='date'
class build_form(forms.ModelForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    licencedate=forms.DateField(widget=DateInput)




    class Meta:
        model= builder_model
        fields=('id','builder_name','licenseno','licencedate','id_proof','up_doc','District','email','phone')