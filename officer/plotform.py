from django import forms

from officer.models import plot_model


class plt_form(forms.ModelForm):
    class Meta:
        model=plot_model
        fields = ('plot','district','village','tt_acres','hm_acres')


