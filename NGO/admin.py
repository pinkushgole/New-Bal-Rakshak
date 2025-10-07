from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NGOInfo
from django.forms import TextInput, Textarea
from django import forms

# Custom form for admin
class NGOInfoAdminForm(forms.ModelForm):
    class Meta:
        model = NGOInfo
        fields = "__all__"
        widgets = {
            'address': Textarea(attrs={'rows':3, 'cols':40}),
        }

class NGOInfoAdmin(UserAdmin):
    form = NGOInfoAdminForm
    model = NGOInfo

    # Fields to display in admin list view
    list_display = ('email', 'name', 'contact', 'city', 'state', 'country', 'pincode', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'state', 'country')

    # Fieldsets for detail/edit view
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
            'fields': (
                'name', 'contact', 'address', 'city', 'state', 'country', 'pincode', 'img'
            )
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')
        }),
    )

    # Fields for adding new NGO
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'name', 'contact', 'address', 'city', 'state', 'country', 'pincode', 'img',
                'password1', 'password2', 'is_staff', 'is_active'
            )}
        ),
    )

    search_fields = ('email', 'name', 'city', 'state', 'country')
    ordering = ('email',)


# Register the model
admin.site.register(NGOInfo, NGOInfoAdmin)