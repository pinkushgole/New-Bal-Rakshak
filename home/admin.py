from django.contrib import admin

# Register your models here.
from .models import ContactUs

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at', 'updated_at')