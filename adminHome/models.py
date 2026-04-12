import django
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class designation_model(models.Model):
    designation=models.CharField(max_length=20)
    class Meta:
        db_table='designation'
    def __str__(self):
        return self.designation

class district_model(models.Model):
    district=models.CharField(max_length=20)
    class Meta:
        db_table='district'
    def __str__(self):
        return self.district


class village_model(models.Model):
    village=models.CharField(max_length=20)
    district=models.ForeignKey(district_model,on_delete=models.CASCADE,default=1)
    class Meta:
        db_table='village'
    def __str__(self):
        return self.village

class quote_model(models.Model):
    quotetype=models.CharField(max_length=20,null=True)
    class Meta:
        db_table='quotetype'
    def __str__(self):
        return self.quotetype




class office_model(models.Model):
    off_name=models.CharField(max_length=20)
    desig=models.ForeignKey(designation_model,on_delete=models.CASCADE)
    dist=models.ForeignKey(district_model,on_delete=models.CASCADE)
    village=models.ForeignKey(village_model,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    mob=models.CharField(max_length=10)
    login = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    regdate=models.DateField(default=django.utils.timezone.now)
    status=models.CharField(max_length=20,default='ACTIVE')

    class Meta:
        db_table = 'office'






class Role_Model(models.Model):
    role_type =  models.CharField(max_length=30)
    login = models.OneToOneField(User, on_delete=models.CASCADE)

class faqQuest_model(models.Model):
    faqQuest=models.CharField(max_length=200)
    faqAns = models.CharField(max_length=200)
    class Meta:
        db_table='faqQuest'
    def __str__(self):
        return self.faqQuest

# class survey_model(models.Model):
#     # appln_no = models.ForeignKey(request_model, on_delete=models.CASCADE)
#     SubmitedBy = models.CharField(max_length=200)
#     Sub_date = models.DateField(default=django.utils.timezone.now)
#     Verifyby = models.CharField(max_length=200)
#     Verify_date = models.DateField(default=django.utils.timezone.now)
#     Verify_status = models.CharField(max_length=200, null=True)
#     rejectreason = models.CharField(max_length=200)
#
#
#     class Meta:
#             db_table = 'survey'
