from django.urls import path
from .views import *

urlpatterns = [

    path('', trainee_list, name='Traineelist'),

    path('<int:id>/', gettraineebyid, name='Trainee_get'),

    path('Update/<int:id>/', update_trainee, name='TraineeCouse'),

    path('HDelete/<int:id>/', HardTraineeDelete, name='HardDelTrainee'),

    path('New/', new_Trainee, name='NewTrainee'),

    path('<str:name>/',getTraineebyname, name='TraineeName'),

]
