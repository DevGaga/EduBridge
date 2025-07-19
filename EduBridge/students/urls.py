from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('student_dashboard/', views.dashboard, name='student_dashboard'),
    path('opportunities/', views.opportunity_list, name='opportunity_list'),
    path('apply/<int:opportunity_id>/', views.apply_to_opportunity, name='apply'),
]
