from django.urls import path
from course.views import *

urlpatterns = [

    path('', course_list, name='Courselist'),

    path('<int:code>/', getcousebycode, name='Course_get'),

    path('Update/<int:code>/', update_course, name='UpdateCouse'),

    path('HDelete/<int:code>/', HardCourseDelete, name='HardDelCourse'),

    path('New/', new_course, name='NewCourse'),

    path('<str:name>/', getcoursebyname, name='CourseName'),

]
