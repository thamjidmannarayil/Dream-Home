from django import forms

from .models import designation_model


class des_form(forms.ModelForm):
    class Meta:
        model=designation_model
        fields=('id','designation')