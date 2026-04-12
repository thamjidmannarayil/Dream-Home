from django import forms

from .models import quotenot_model


class notif_form(forms.ModelForm):
    class Meta:
        model=quotenot_model
        fields = ('QuotationType','quote_code','quote_name','Project','open_date','close_date','quote_doc1','quote_doc2','description')

