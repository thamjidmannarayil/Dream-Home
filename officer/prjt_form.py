from django import forms

from .models import project_model

plot_status=[('Yes','Yes'),('No','No')]
class proj_form(forms.ModelForm):
    plot=forms.CharField(widget=forms.RadioSelect(choices=plot_status))
    class Meta:
        model=project_model
        fields = ('id','ProjectName','plot_status','scheme','strt_dt','end_dt','house_no','amount_tt','normal_fnd','other_fnd','criteria','sq_feet','no_rooms','hm_details','image1','image2','sub_date','status')


