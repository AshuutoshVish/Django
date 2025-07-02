from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from .models import Student, Enrollment
from .forms import StudentForm, EnrollmentForm

def home(request):
    students = Student.objects.all()
    enrollments = Enrollment.objects.all()
    return render(request, 'main/home.html', {'students': students, 'enrollments' : enrollments})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'main/add_student.html', {'form': form})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id = student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'main/edit_student.html', {'form': form, 'title':'Edit Student'})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.success(request, "Student deleted successfully.")
    return redirect('home')

def add_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EnrollmentForm()
    return render(request, 'main/add_enrollment.html', {'form':form, 'title' : 'Add Enrollment'})

def edit_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, 'main/edit_enrollment.html', {'form': form, 'title': 'Edit Enrollment'})

def delete_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    enrollment.delete()
    messages.success(request, "Enrollment deleted successfully.")
    return redirect('home')
