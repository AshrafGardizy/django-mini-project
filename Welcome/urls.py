from django.urls import path
from .views import HelloMessage

urlpatterns = [
    path('',HelloMessage.as_view(),name='index'),
  
]