from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'role', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib import admin

class OfficeHeadAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_office_head

office_head_admin_site = OfficeHeadAdminSite(name='office_head_admin')
