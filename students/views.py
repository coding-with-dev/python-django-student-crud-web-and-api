from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Students
from .forms import StudentForm

def list_students(request):
    students = Students.objects.all().order_by('-pk')
    page_data = {
        "students": students
    }
    return render(request, 'students/list.html', page_data)

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect(request.path)        
    else:
        form = StudentForm()
    
    return render(request, 'students/add.html', {'form': form})

def edit_student(request, id):
    student = get_object_or_404(Students, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect(request.path)        
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit.html', {'form': form, 'student': student})

def details_student(request, id):
    student = get_object_or_404(Students, id=id)
    return render(request, 'students/details.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Students, id=id)
    student.delete()
    return redirect('list_students')