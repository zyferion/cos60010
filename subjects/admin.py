from django.contrib import admin

# Register your models here.
from .models import Subject, Enrolment

# Register your models here.
admin.site.register(Subject)
admin.site.register(Enrolment)
