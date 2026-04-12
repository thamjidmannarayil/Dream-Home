from django import forms

from adminHome.models import survey_model


class surv_form(forms.ModelForm):
    class Meta:
        model=survey_model
        fields=('id','appln_no','SubmitedBy','Sub_date','Verifyby','Verify_date','rejectreason')

      