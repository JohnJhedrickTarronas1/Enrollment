from django.db import models


class Student(models.Model):
    STATUS_CHOICES = [
        ('Enrolled', 'Enrolled'),
        ('Pending', 'Pending'),
        ('Inactive', 'Inactive'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    student_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=150)
    grade_level = models.CharField(max_length=50, default='Grade 11')
    section = models.CharField(max_length=50, default='ICT - A')
    school_year = models.CharField(max_length=20, default='2026-2027')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Enrolled')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Male')
    email = models.EmailField()
    contact_number = models.CharField(max_length=30)
    home_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.full_name} ({self.student_id})"
