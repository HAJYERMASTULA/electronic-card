from django.contrib import admin
from .models import Student,Card

# Register your models here.
#class StudentAdmin(admin.ModelAdmin):
   # list_display = ("student_name","gender","course","session","date_of_birth","address","religion","telephone_no","nationality","marital_status")

admin.site.register(Student)
admin.site.register(Card)
