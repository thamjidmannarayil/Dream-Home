from django import forms

from builder.models import reqapply_model


class reqapply_form(forms.ModelForm):
    class Meta:
        model=reqapply_model
        fields=('bid_amt','doc1','doc2')
