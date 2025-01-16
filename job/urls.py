from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='job-list'),
    path('edit/<int:job_id>/', views.job_edit, name='job-edit'),
    path('job-delete/<int:id>/', views.job_delete, name='job-delete'),
]