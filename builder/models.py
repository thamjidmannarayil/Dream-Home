import django
from django.db import models
from registration.models import builder_model
from officer.models import quotenot_model


class reqapply_model(models.Model):
    quote_code = models.ForeignKey(quotenot_model, on_delete=models.CASCADE)
    builderid = models.ForeignKey(builder_model, on_delete=models.CASCADE)
    bid_amt = models.IntegerField()
    doc1 = models.FileField(upload_to="images")
    doc2 = models.FileField(upload_to="images")
    subdate=models.DateField(default=django.utils.timezone.now)
    bid_status=models.CharField(max_length=20,default='New')
    work_status=models.CharField(max_length=20,default='New')



    class Meta:
        db_table = 'reqapply'