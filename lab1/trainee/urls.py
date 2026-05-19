from django.urls import path,include
from .views import *

urlpatterns = [
    path('API/',include('trainee.api.urls')),

    path('', Traineelist.as_view(), name='Traineelist'),

    path('<int:id>/', gettraineebyid, name='Trainee_get'),

    path('Update/<int:id>/', update_trainee, name='TraineeUpdate'),

    path('HDelete/<int:id>/', HardTraineeDelete, name='HardDelTrainee'),

    path('SDelete/<int:id>',softdelete,name="SoftDelete"),

    path('New/', new_Trainee, name='NewTrainee'),

    path('<str:name>/',getTraineebyname, name='TraineeName'),

]
