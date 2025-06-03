from django.contrib import admin
from .models import Student, Department

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email')
admin.site.register(Student)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','faculty', 'no.of.std')
admin.site.register(Department)