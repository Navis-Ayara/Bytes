from django.urls import path
from django.contrib.auth import views as auth_views
from .views import registration

urlpatterns = [
    path('register/', registration.as_view(), name='register'),
]