from django.contrib import admin

# Register your models here.

from membership.models import Student
admin.site.register(Student)