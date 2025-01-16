from django.contrib import admin

# Register your models here.
from .models import AgentManagementNewAgentModel

@admin.register(AgentManagementNewAgentModel)
class AgentManagementNewAgentAdmin(admin.ModelAdmin):
    list_display = ('agent_id', 'name', 'phone', 'district', 'place')