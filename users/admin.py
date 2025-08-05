from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users
# Register your models here.

class HXUsersAdmin(UserAdmin):
    model = Users
    list_display = ['email', 'username','is_staff', 'is_superuser']
    fieldsets = ((None,{'fields':('email', 'password')}),
                 ('profile',{'fields':('username','name','bio','profile_image')}),
                 ('permission',{'fields':('is_active','is_staff','is_superuser','groups','user_permission')}),)
    add_fieldsets = ((None,{'classes':('wide',),
                            'fields':('email','username','password1','password2','is_staff', 'is_active')}),)
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(Users, HXUsersAdmin)
