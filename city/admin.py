from django.contrib import admin

# Register your models here.
# from simpleui.templatetags.simpletags import custom_button

from city.models import *

# admin.site.register(City)

@admin.register(City)
class admincity(admin.ModelAdmin):
    list_display = ('city','province','tags')
    list_filter = ('province',)
    # actions = ['make_copy', 'custom_button']
    # custom_button.short_description = '测试按钮'

