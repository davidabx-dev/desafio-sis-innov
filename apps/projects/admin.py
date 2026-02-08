from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_name', 'status', 'owner', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'client_name', 'description')
    readonly_fields = ('created_at', 'updated_at')