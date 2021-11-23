from django.contrib import admin
from WebApp.models import Registationproject
# Register your models here.
#class RegistationprojectAdmin(admin.ModelAdmin):
    #list_display = ['username','firstname','lastname','email','password','password1']

admin.site.register(Registationproject)
