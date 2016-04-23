
from django.contrib import admin,messages
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.forms import ModelForm
from .models import *
# Register your models here.

class UserAdmin(ModelAdmin):
    search_fields = ['name','id']
    list_display = ('id', 'name',)
    list_display_links = ('name',)
class RoleAdmin(ModelAdmin):
    search_fields = ['name','id']
    list_display = ('id', 'name')
    list_display_links = ('name',)

class PermissionAdmin(ModelAdmin):
    search_fields = ['name','id']
    list_display = ('id', 'name')
    list_display_links = ('name',)

admin.site.register(User,UserAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Permission,PermissionAdmin)
