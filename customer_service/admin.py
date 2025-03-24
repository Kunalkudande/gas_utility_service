from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'request_type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('status', 'request_type', 'submitted_at')
    search_fields = ('details', 'user__username')
    date_hierarchy = 'submitted_at'