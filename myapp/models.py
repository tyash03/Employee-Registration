from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=30, null=True)
    desg = models.CharField(max_length=30, null=True)
    salary = models.FloatField(null=True)
    photo = models.ImageField(upload_to='images/', default='default.jpg')
    def __str__(self):
        return (self.ename)  

