from django.db import models
from course.models import Courses

# Create your models here.
class Trainee(models.Model):
    id= models.AutoField(primary_key=True,verbose_name='ID',help_text='Trainee_ID')
    name=models.CharField(max_length=100,verbose_name='Name',help_text='Trianee Name')
    email=models.EmailField(max_length=100,verbose_name='Email')
    phone=models.CharField(max_length=15)
    image= models.ImageField(upload_to='Trainee_Photo',blank=True,null=True)
    Course=models.ForeignKey(Courses,on_delete=models.CASCADE)

    def __str__(self):
        return self.name