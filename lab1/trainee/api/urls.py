from django.urls import path,include
from .views import trainee_json,listtrainee,Traineecreate,Traineeupdate,Traineeviewset
from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


drouter=DefaultRouter()
drouter.register(r'VS',Traineeviewset,basename='VS')

urlpatterns=[
    path('',include(drouter.urls)),
    path('json/',trainee_json),
    path('List/',listtrainee),
    path('List/<int:id>/',listtrainee),
    path('Add/',Traineecreate.as_view()),
    path('Update/<int:id>/',Traineeupdate.as_view()),
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),

]