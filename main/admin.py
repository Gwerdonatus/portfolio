from django.contrib import admin
from .models import Project
from .models import ContactMessage


admin.site.register(Project)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email')
