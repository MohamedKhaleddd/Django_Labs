from django.urls import path
from trainee.views import *

urlpatterns = [
    path('',trainee_list,name= 'Courselist'),
    path('<str:name>/',add_trainee,name= 'AddCourse'),
    path('Update/<int:id>/',update_trainee,name= 'UpdateCouse'),
    path('Delete/<int:id>/',delete_trainee,name= 'DeleteCourse'),
]
