from django import forms

from officer.models import surveyreport_model


class survey_form(forms.ModelForm):
    class Meta:
        model=surveyreport_model
        fields = ('submittedby','sub_date','verifyby','verify_date','verifystatus','reject_reason')

