# school/views.py
from django.shortcuts import render, redirect
from .models import Student, Application, Payment
from .forms import StudentForm, ApplicationForm, PaymentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'school/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'school/student_form.html', {'form': form})

# ... define other views as needed