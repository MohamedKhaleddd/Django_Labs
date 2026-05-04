from django.urls import path
from course.views import *

urlpatterns = [
    path('',course_list,name= 'Courselist'),
    path('<str:name>/',add_course,name= 'AddCourse'),
    path('Update/<int:id>/',update_course,name= 'UpdateCouse'),
    path('Delete/<int:id>/',delete_course,name= 'DeleteCourse'),
]
