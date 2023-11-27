from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'name',
        'level',
        'date_joined'
    )
    search_fields = ('user_id', 'name')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)  # Admin페이지의 GROUP삭제