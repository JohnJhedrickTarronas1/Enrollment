
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=150)),
                ('grade_level', models.CharField(default='Grade 11', max_length=50)),
                ('section', models.CharField(default='ICT - A', max_length=50)),
                ('school_year', models.CharField(default='2026-2027', max_length=20)),
                ('status', models.CharField(choices=[('Enrolled', 'Enrolled'), ('Pending', 'Pending'), ('Inactive', 'Inactive')], default='Enrolled', max_length=20)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=30)),
                ('home_address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
