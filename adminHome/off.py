from django import forms

from .models import office_model

gender=[('M','Male'),('F','Female'),('T','Transgender')]

class off_form(forms.ModelForm):
    gender=forms.CharField(widget=forms.RadioSelect(choices=gender))
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=office_model
        fields=('id','off_name','desig','dist','village','address','mob','regdate','status')

