from django.db import models

class studentModel(models.Model):
    
    Name = models.CharField(max_length=100,null=True)
    Depertment = models.CharField(max_length=20, null=True)
    Passing_Year = models.CharField(max_length=4, null=True)
    
class teacherModel(models.Model):
    
    Name = models.CharField(max_length=100,null=True)
    Depertment = models.CharField(max_length=10, null=True)
    Contact = models.IntegerField(max_length=11, null=True) 
    
    