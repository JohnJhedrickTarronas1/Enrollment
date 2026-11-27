from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'full_name', 'grade_level', 'section', 'school_year', 'status')
    search_fields = ('student_id', 'full_name', 'email', 'section')
    list_filter = ('status', 'grade_level', 'school_year')
