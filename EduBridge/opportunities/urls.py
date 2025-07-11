from django.urls import path
from . import views

app_name = 'opportunities'

urlpatterns = [
    path('', views.public_list, name='list'),
]
