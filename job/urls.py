from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    path('', views.JobsList.as_view(), name='job-list'),
    path('edit/<int:job_id>/', views.job_edit, name='job-edit'),
    path('job-delete/<int:id>/', views.job_delete, name='job-delete'),
]