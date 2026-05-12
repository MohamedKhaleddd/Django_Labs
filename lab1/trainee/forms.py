from django import forms
from course.models import *
from .models import *

class TraineeForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=150)
    phone=forms.CharField(max_length=15)
    image= forms.ImageField()
    Course=forms.ChoiceField(choices=[(cou.code,cou.name)for cou in Courses.objects.all()])

class TraineeFormModel(forms.ModelForm):
    class Meta:
        model=Trainee
        fields='__all__'