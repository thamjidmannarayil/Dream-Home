import django
from django.contrib.auth.models import User
from django.db import models

from registration.models import applicant_model
from adminHome.models import district_model, village_model


# Create your models here.

class request_model(models.Model):
    appln_no = models.IntegerField( null=True)
    applicantid = models.ForeignKey(applicant_model, on_delete=models.CASCADE)
    adhar_no = models.IntegerField()
    gender = models.CharField(max_length=200)
    age = models.IntegerField()
    photo = models.FileField(upload_to="images")
    app_job = models.CharField(max_length=200)
    idproof = models.FileField(upload_to="images")
    plot_available = models.CharField(max_length=200)
    cent = models.IntegerField()
    survey_no = models.IntegerField()
    plot_distid = models.ForeignKey(district_model, on_delete=models.CASCADE, default=1)
    plot_villageid = models.ForeignKey(village_model, on_delete=models.CASCADE, default=1)
    location = models.CharField(max_length=200)
    loc_type = models.CharField(max_length=200)
    rationcard_no = models.IntegerField()
    status=models.CharField(max_length=20,default='New')
    member_no=models.IntegerField(null=True)
    Gov_emp_no=models.IntegerField(null=True)
    Anual_income=models.IntegerField(null=True)
    Income_certf=models.CharField(max_length=200,null=True)
    applydate= models.DateField(default=django.utils.timezone.now)
    Verify_status=models.CharField(max_length=200,null=True)
    Work_status=models.CharField(max_length=200,null=True)

    class Meta:
        db_table = 'request'





class complaint_model(models.Model):
    com_id = models.IntegerField(null=True)
    appln_no = models.ForeignKey(applicant_model, on_delete=models.CASCADE)
    complaints = models.TextField(max_length=2000)
    send_date = models.DateField(default=django.utils.timezone.now)
    status = models.CharField(max_length=20, default='INACTIVE')

