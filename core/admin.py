from django.contrib import admin
from .models import Module, Permission, Role, UserRole

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'module')
    list_filter = ('module',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('permissions',)

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
