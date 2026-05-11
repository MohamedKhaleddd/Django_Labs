from django.db import models

# Create your models here.
class Courses(models.Model):
    code= models.AutoField(primary_key=True,verbose_name="Course Code")
    name=models.CharField(max_length=50,verbose_name="Course name")
    description= models.TextField(null=True)
    tool=models.CharField(max_length=100,verbose_name="Course tools",null=True)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    create_date=models.DateField(auto_now_add=True,verbose_name="Insert Date")
    update_date=models.DateField(auto_now=True,verbose_name="Update Date")
    image=models.ImageField(blank=True,null=True)
    def __str__(self):
        return self.name
