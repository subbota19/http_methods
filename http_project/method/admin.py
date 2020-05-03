from django.contrib import admin
from .models import MyUser


class AdminMyUser(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'created', 'updated']
    list_filter = ['name', 'year', 'created']
    search_fields = ['name']


admin.site.register(MyUser, AdminMyUser)
