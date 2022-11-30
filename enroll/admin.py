from django.contrib import admin
from .models import StudentRegistration

# Register your models here.
@admin.register(StudentRegistration)
class AdminStudentRegistration(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'password')