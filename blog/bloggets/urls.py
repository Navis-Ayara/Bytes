from django.urls import path
from .views import registration

urlpatterns = [
    path('register/', registration.as_view(), name='register'),
]