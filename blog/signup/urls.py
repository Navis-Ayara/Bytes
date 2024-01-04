from django.urls import path
from .views import User_SignUp

##### path goes here

urlpatterns = [
    path('registration/', User_SignUp.as_view(), name='registration'), # signup/path 
] 
