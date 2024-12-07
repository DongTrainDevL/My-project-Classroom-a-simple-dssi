from django.contrib import admin

from .models import *

# Register your models here.
# admin/1234
admin.site.register(Course)
admin.site.register(Student)