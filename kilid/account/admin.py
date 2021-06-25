import os
from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.hashers import make_password
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'my_file', 'size','my_name')
    fieldsets = [
      ('personal info', {
          'fields':['user_name','password']
      }),
      ('extra info', {
          'fields': ['my_file', 'size','my_name']
      }),
    ]
   
    
    search_fields = ('user_name', 'my_file', 'size','my_name')
    list_filter = ('user_name', 'my_file', 'size','my_name')

    def save_model(self, request, obj, form, change):
        password = form.cleaned_data['password']
        obj.password = make_password(password)
        obj.size = form.cleaned_data['my_file'].size
        obj.my_name = form.cleaned_data ['my_file'].name
        obj.save()

admin.site.register(CustomUser, CustomUserAdmin)
