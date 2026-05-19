from rest_framework import serializers
from course.models import *
from trainee.models import Trainee

class CoursesSerializers(serializers.ModelSerializer):
    class Meta:
        model= Courses
        fields=['code','name']

class TraineeSerializers(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    phone=serializers.CharField(max_length=15)
    create_date=serializers.DateField(read_only=True)
    update_date=serializers.DateTimeField(read_only=True)
    image= serializers.ImageField(required=False,allow_null=True)
    Course=serializers.PrimaryKeyRelatedField(queryset=Courses.objects.all())
    is_active=serializers.BooleanField(default=True)

    def create(self,validated_data):
        return Trainee.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        for attr,value in validated_data.items():
            setattr(instance,attr,value)

        instance.save()
        return instance