from django.urls import path
from . import views

app_name = 'institution'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_opportunity, name='create_opportunity'),
    # Add more paths like 'edit/<id>/' and 'delete/<id>/' if needed
]
