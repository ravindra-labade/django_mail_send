from django.urls import path
from .views import  sending_mail


urlpatterns = [
    path('', sending_mail),
]
