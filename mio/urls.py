"""mio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from mio_auth import views as auth_views
from . import views 
from job import views as job_views
from mio_customer import views as customer_views
from job.views import job_list
from mio_customer.views import CreateCustomer

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', auth_views.Login.as_view(), name='login'),
    path('login-authentication-check-secret-key-api', auth_views.CheckAuthenticateSecretKeyAPI.as_view()),
    path('index', auth_views.AgentsList.as_view(), name='index'),
    path('faq', auth_views.AgentsList.as_view(), name='faq'),
    path('agents-list/', auth_views.AgentsList.as_view(), name='agents-list'),
    path('new-agent/', auth_views.NewAgent.as_view(), name='new-agent'),
    path('leads-kanban', auth_views.AgentsList.as_view(), name='leads_kanban'),
    path('job-management/', job_views.job_list, name='job-management-list'),  
    path('job-management/edit/<int:job_id>/', job_views.job_edit, name='job-edit'),
    path('job-management/delete/<int:id>/', job_views.job_delete, name='job-delete'), 
    path('job/create/', job_views.job_create, name='job-create'),
     path('job/list/', job_views.job_list, name='job-list'),
     #enter customer_module url
    path('customer-list/', customer_views.CustomerList.as_view(), name='customer-list'),
  path('create-customer/', CreateCustomer.as_view(), name='create-customer'),
]
