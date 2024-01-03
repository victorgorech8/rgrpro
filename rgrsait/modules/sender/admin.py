from django.contrib import admin
from .models import SQLq

class SQLqAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(SQLq,SQLqAdmin)
