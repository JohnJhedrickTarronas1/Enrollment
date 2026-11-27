from datetime import date
from django.core.management.base import BaseCommand
from students.models import Student


class Command(BaseCommand):
    help = 'Seeds initial student enrollment records matching the roster UI'

    def handle(self, *args, **options):
        sample_students = [
            {
                'student_id': '123-456',
                'full_name': 'John Jhedrick Tarronas',
                'grade_level': 'Grade 12',
                'section': 'ICT - A',
                'school_year': '2026-2027',
                'status': 'Enrolled',
                'date_of_birth': date(2005, 10, 15),
                'gender': 'Male',
                'email': 'jhedricktarronas0@gmail.com',
                'contact_number': '0909 083 8434',
                'home_address': 'Lucena City, Quezon',
            },
            {
                'student_id': '123-457',
                'full_name': 'Emmanuel Mirandilla',
                'grade_level': 'Grade 12',
                'section': 'ICT - C',
                'school_year': '2026-2027',
                'status': 'Enrolled',
                'date_of_birth': date(2004, 3, 28),
                'gender': 'Male',
                'email': 'Emman@gmail.com',
                'contact_number': '0999 567 0987  ',
                'home_address': 'Lucena City, Quezon',
            },
            {
                'student_id': '1234-458',
                'full_name': 'Elisha Mae Sarto',
                'grade_level': 'Grade 11',
                'section': 'ICT - B',
                'school_year': '2026-2027',
                'status': 'Enrolled',
                'date_of_birth': date(2007, 11, 16),
                'gender': 'Female',
                'email': 'Elisha@gmail.com',
                'contact_number': '0911 222 3333',
                'home_address': 'Tayabas, Quezon',
            },
            {
                'student_id': '123-459',
                'full_name': 'Derick Miranda',
                'grade_level': 'Grade 11',
                'section': 'ICT - B',
                'school_year': '2026-2027',
                'status': 'Enrolled',
                'date_of_birth': date(2007, 10, 13),
                'gender': 'Male',
                'email': 'Derick@gmail.com',
                'contact_number': '0965 647 8976',
                'home_address': 'Sariaya, Quezon',
            },
        ]

        created_count = 0
        for data in sample_students:
            _, created = Student.objects.update_or_create(
                student_id=data['student_id'],
                defaults=data,
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Seeded {len(sample_students)} students ({created_count} newly created).')
        )
