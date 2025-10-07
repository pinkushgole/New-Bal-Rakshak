from django.contrib import admin
from .models import ChildrenInfo

class ChildrenInfoAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'person_contact', 'city', 'state', 'country', 'pincode', 'is_safe', 'created_at')
    list_filter = ('is_safe', 'state', 'country', 'created_at')
    search_fields = ('person_name', 'person_contact', 'address', 'city', 'state', 'country', 'pincode')
    readonly_fields = ('created_at', 'updated_at')  # Prevent editing auto fields

    # Optional: fieldsets for better detail/edit view
    fieldsets = (
        (None, {'fields': ('person_name', 'person_contact', 'is_safe')}),
        ('Address Info', {'fields': ('address', 'city', 'state', 'country', 'pincode')}),
        ('Additional Info', {'fields': ('details', 'img')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )

# Register the model
admin.site.register(ChildrenInfo, ChildrenInfoAdmin)