from django import forms

from .models import quote_model


class qt_form(forms.ModelForm):
    class Meta:
        model=quote_model
        fields=('id','quotetype')