from django.db.models import Q
from django.shortcuts import render
from .models import Student


def roster_view(request):
    query = request.GET.get('q', '').strip()
    selected_id = request.GET.get('student', '').strip()

    students = Student.objects.all()
    if query:
        students = students.filter(
            Q(full_name__icontains=query)
            | Q(student_id__icontains=query)
            | Q(section__icontains=query)
        )

    selected_student = None
    if selected_id:
        selected_student = students.filter(student_id=selected_id).first()
    if not selected_student:
        selected_student = students.first()

    school_year = selected_student.school_year if selected_student else '2026-2027'

    context = {
        'students': students,
        'selected_student': selected_student,
        'query': query,
        'school_year': school_year,
    }
    return render(request, 'students/roster.html', context)
