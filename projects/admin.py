from django.contrib import admin
from .models import Project, Tool

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    pass

class ToolAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tool, ToolAdmin)