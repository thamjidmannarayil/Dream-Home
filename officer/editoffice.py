from django import forms

from adminHome.models import office_model

gender=[('M','Male'),('F','Female'),('T','Transgender')]

class editoff_form(forms.ModelForm):
    gender=forms.CharField(widget=forms.RadioSelect(choices=gender))

    class Meta:
        model=office_model
        fields=('off_name','gender','desig','dist','village','address','mob')