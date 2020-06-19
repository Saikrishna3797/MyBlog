from django.contrib import admin
from projects.models import Project,ProjectCategory
# Register your models here.

class projectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project,projectAdmin)
admin.site.register(ProjectCategory,projectAdmin)