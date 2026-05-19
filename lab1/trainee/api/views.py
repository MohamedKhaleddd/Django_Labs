from django import views
from trainee.models import *
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView,get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializer import TraineeSerializers

class Traineeviewset(viewsets.ViewSet):
    permission_classes= [IsAuthenticated]
    def list(self,request):
        queryset=Trainee.objects.select_related('Course').filter(is_active=True)
        serializer=TraineeSerializers(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer=TraineeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk):
        queryset=Trainee.objects.select_related('Course').all()
        trainee=get_object_or_404(queryset,pk=pk)
        traineesr=TraineeSerializers(trainee)
        return Response(data=traineesr.data,status=status.HTTP_200_OK)
    def update(self,request,pk):
        trainee=get_object_or_404(Trainee,pk=pk)
        serializer=TraineeSerializers(instance=trainee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        trainee=get_object_or_404(Trainee,pk=pk)
        trainee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Traineecreate(APIView):
    def post(self,request,formate=None):
        traineeser=TraineeSerializers(data=request.data)
        if traineeser.is_valid():
            traineeser.save()
            return Response( data = {"msg":"Trainee added","data": traineeser.data},
                            status=status.HTTP_201_CREATED)

        return Response(traineeser.errors,status=status.HTTP_400_BAD_REQUEST)
    

class Traineeupdate(UpdateAPIView):
    queryset= Trainee.objects.filter(is_active=True)
    lookup_field= 'id'
    serializer_class=TraineeSerializers


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def listtrainee(request,id=None):
    if id:
        trainee=Trainee.objects.get(pk=id)
        traineeserializer=TraineeSerializers(trainee)
        return Response(data=traineeserializer.data,status=status.HTTP_200_OK)


    else:
        trainee=Trainee.objects.select_related('Course').filter(is_active=True)
        traineeserializer=TraineeSerializers(trainee,many=True)
        return Response(data=traineeserializer.data,status=status.HTTP_200_OK)




def trainee_json (request):
    trainees=Trainee.objects.values('id','name')
    return JsonResponse(list(trainees),safe=False)