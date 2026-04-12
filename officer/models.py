import django
from django.db import models

from registration.models import applicant_model
from adminHome.models import district_model, village_model


from adminHome.models import quote_model
from applicant.models import complaint_model, request_model


class project_model(models.Model):
    ProjectName=models.CharField(max_length=200, null=True)
    plot_status=models.BooleanField()
    scheme=models.CharField(max_length=20)
    strt_dt=models.DateField()
    end_dt = models.DateField()
    house_no=models.IntegerField()
    amount_tt=models.IntegerField()
    normal_fnd=models.IntegerField()
    other_fnd=models.IntegerField()
    criteria=models.TextField(max_length=100)
    sq_feet = models.IntegerField()
    no_rooms = models.IntegerField()
    hm_details = models.CharField(max_length=200)
    image1=models.FileField(upload_to="images")
    image2 = models.FileField(upload_to="images")
    sub_date=models.DateField(default=django.utils.timezone.now)
    status=models.CharField(max_length=20,default='ACTIVE')


    class Meta:
        db_table = 'project'
    def __str__(self):
        return self.scheme




class plot_model(models.Model):
    project = models.ForeignKey(project_model, on_delete=models.CASCADE, default=1)
    plot=models.CharField(max_length=20)
    district = models.ForeignKey(district_model, on_delete=models.CASCADE, default=1)
    village=models.ForeignKey(village_model,on_delete=models.CASCADE)
    tt_acres=models.IntegerField()
    hm_acres=models.IntegerField()


    class Meta:
        db_table = 'plot'






class quotenot_model(models.Model):
    quote_code = models.IntegerField( null=True)
    Project = models.ForeignKey(project_model, on_delete=models.CASCADE)
    quote_name = models.CharField(max_length=200)
    open_date=models.DateField(default=django.utils.timezone.now)
    close_date=models.DateField(default=django.utils.timezone.now)
    QuotationType = models.ForeignKey(quote_model, on_delete=models.CASCADE)
    quote_doc1 = models.FileField(upload_to="images")
    quote_doc2 = models.FileField(upload_to="images")
    description = models.CharField(max_length=200)
    status=models.CharField(max_length=20,default='New')


    class Meta:
        db_table = 'notification'

class complrep_model(models.Model):
    complaint = models.ForeignKey(complaint_model, on_delete=models.CASCADE, default=1)
    reply = models.CharField(max_length=2000)
    status=models.CharField(max_length=20,default='successfully replied')


    class Meta:
        db_table = 'complaintreply'




class surveyreport_model(models.Model):
    appln_no = models.ForeignKey(applicant_model, on_delete=models.CASCADE)
    submittedby =models.CharField(max_length=200)
    sub_date=models.DateField(default=django.utils.timezone.now)
    verifyby = models.CharField(max_length=200)
    verify_date=models.DateField(default=django.utils.timezone.now)
    verifystatus=models.CharField(max_length=20,default='New')
    reject_reason = models.CharField(max_length=200)


    class Meta:
        db_table = 'surveyreport'




