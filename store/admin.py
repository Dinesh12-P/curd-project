from django.contrib import admin
from store.models import *

# admin.site.register(Task)
@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display=[
        'title','description','status',
    ]
    list_per_page = 5
    search_fields = ('title',)