from django import forms

from .models import faqQuest_model


class fq_form(forms.ModelForm):
    faqQuest=forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 75}))
    faqAns=forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 75}))
    class Meta:
        model=faqQuest_model
        fields=('id','faqQuest','faqAns')

