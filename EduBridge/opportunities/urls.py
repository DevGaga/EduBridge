from django.urls import path
from . import views

app_name = 'opportunities'

urlpatterns = [
    path('', views.public_list, name='opportunities'),
    path('<int:pk>/', views.detail, name='detail'),
]
