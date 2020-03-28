from django.contrib import admin

# Register your models here.
from user.models import *
@admin.register(User)
class Adminuser(admin.ModelAdmin):
    verbose_name = '昵称'
    list_display = ('uname', 'upass', 'uemail')
    # fields = ('uname', 'upass', 'uemail')
