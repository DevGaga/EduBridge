from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('<int:pk>/', views.application_detail, name='detail'),
]
