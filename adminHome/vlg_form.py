from django import forms

from .models import village_model


class vlg_form(forms.ModelForm):
    class Meta:
        model=village_model
        fields=('id','village')