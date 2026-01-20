from django.shortcuts import render, redirect
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
        validation_errors = []
        success_message = ''

        fullname = request.POST.get('fullname')
        email_addr = request.POST.get('email_addr')
        mobile_no = request.POST.get('mobile_no')
        age = request.POST.get('age')
        photo = request.FILES.get('photo')

        if not fullname: 
            validation_errors.append('Please enter fullname')

        if not email_addr: 
            validation_errors.append('Please enter email address')

        if not mobile_no: 
            validation_errors.append('Please enter mobile no')

        if not age: 
            validation_errors.append('Please enter age')

        if not validation_errors:
            Students.objects.create(
                name = fullname, 
                email = email_addr,
                age = age,
                mobile = mobile_no,
                photo = photo
            )

        if not validation_errors:
            success_message = "Student details added successfully"
            request.POST = []

        page_data = {
            "errors": validation_errors,
            "success": success_message
        }
        return render(request, 'students/add.html', page_data)
    else:    
        return render(request, 'students/add.html')

def edit_student(request):
    return render(request, 'students/edit.html')

def details_student(request):
    return render(request, 'students/details.html')

def add_student_model_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect(request.path)
        
    else:
        form = StudentForm()
    
    return render(request, 'students/add-model-base.html', {'form': form})
