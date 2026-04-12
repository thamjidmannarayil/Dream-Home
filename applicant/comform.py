from django import forms

from applicant.models import complaint_model


class com_form(forms.ModelForm):
    complaints = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 100}))
    class Meta:
        model=complaint_model
        fields=('id','complaints')

