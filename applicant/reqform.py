from django import forms
from django.forms import models

from registration.models import applicant_model

from applicant.models import request_model


class req_form(forms.ModelForm):
    class Meta:
        model=request_model
        fields=('adhar_no','gender','age','photo','app_job','idproof','plot_available','cent','survey_no','plot_distid','plot_villageid','location','loc_type','rationcard_no','member_no','Gov_emp_no','Anual_income','Income_certf','applydate')

