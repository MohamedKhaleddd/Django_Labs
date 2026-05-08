from django.db import models

# Create your models here.
class Trainee(models.Model):
    id= models.IntegerField(primary_key=True,verbose_name='ID',help_text='Trainee_ID')
    name=models.CharField(max_length=100,verbose_name='Name',help_text='Trianee Name')
    #test=models.TextField()