from django import forms

from .models import district_model


class dist_form(forms.ModelForm):
    class Meta:
        model=district_model
        fields=('id','district')