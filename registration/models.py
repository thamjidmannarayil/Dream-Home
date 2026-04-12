import django
from django.contrib.auth.models import User
from django.db import models

from adminHome.models import district_model


# Create your models here.
# builder registration
# applicant regiration
class builder_model(models.Model):
    builder_name=models.CharField(max_length=20)
    licenseno=models.IntegerField()
    licencedate = models.DateField()
    id_proof=models.FileField(upload_to="images")
    up_doc=models.FileField(upload_to="images")
    District = models.ForeignKey(district_model, on_delete=models.CASCADE)
    email= models.EmailField(max_length=20)
    phone=models.CharField(max_length=20)
    login = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    reg_date = models.DateField(default=django.utils.timezone.now)
    status = models.CharField(max_length=20,default='INACTIVE')


    class Meta:
        db_table = 'builder'


    # def __str__(self):
    #     return self.builder_name




class applicant_model(models.Model):
    applicant_name=models.CharField(max_length=20)
    address=models.TextField(max_length=20)
    mobile=models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    login = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    reg_date = models.DateField(default=django.utils.timezone.now)
    status = models.CharField(max_length=20,default='INACTIVE')


    class Meta:
        db_table = 'applicant'

    def __str__(self):
        return self.applicant_name