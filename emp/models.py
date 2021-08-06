from django.db import models

# Create your models here.
class Exmpmodel(models.Model):
    empname=models.CharField(max_length=100)
    class Meta:
        db_table='empapp_employeetab'


class Employeemodel(models.Model):
    empname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    salary=models.IntegerField()
    class Meta:
        db_table='employee'
