from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models_old import Student
from .forms import StudentForm  # Make sure to create the form in forms.py

# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Create a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the list of students
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

# Update an existing student
def student_update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

# Delete a student
def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})


from .models_old import Contact
from .forms import ContactForm  # Create the ContactForm in forms.py

# List all contacts for a student
def contact_list(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    contacts = student.contacts.all()
    return render(request, 'contact_list.html', {'contacts': contacts, 'student': student})

# Create a new contact
def contact_create(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.student = student
            contact.save()
            return redirect('contact_list', student_id=student.id)
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form, 'student': student})

# Update an existing contact
def contact_update(request, student_id, contact_id):
    student = get_object_or_404(Student, pk=student_id)
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list', student_id=student.id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_form.html', {'form': form, 'student': student})

# Delete a contact
def contact_delete(request, student_id, contact_id):
    student = get_object_or_404(Student, pk=student_id)
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list', student_id=student.id)
    return render(request, 'contact_confirm_delete.html', {'contact': contact, 'student': student})
from .models_old import MedicalRecord
from .forms import MedicalRecordForm  # Create the MedicalRecordForm in forms.py

# List all medical records for a student
def medical_record_list(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    medical_records = student.medical_records.all()
    return render(request, 'medical_record_list.html', {'medical_records': medical_records, 'student': student})

# Create a new medical record
def medical_record_create(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            medical_record = form.save(commit=False)
            medical_record.student = student
            medical_record.save()
            return redirect('medical_record_list', student_id=student.id)
    else:
        form = MedicalRecordForm()
    return render(request, 'medical_record_form.html', {'form': form, 'student': student})

# Update an existing medical record
def medical_record_update(request, student_id, medical_record_id):
    student = get_object_or_404(Student, pk=student_id)
    medical_record = get_object_or_404(MedicalRecord, pk=medical_record_id)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list', student_id=student.id)
    else:
        form = MedicalRecordForm(instance=medical_record)
    return render(request, 'medical_record_form.html', {'form': form, 'student': student})

# Delete a medical record
def medical_record_delete(request, student_id, medical_record_id):
    student = get_object_or_404(Student, pk=student_id)
    medical_record = get_object_or_404(MedicalRecord, pk=medical_record_id)
    if request.method == 'POST':
        medical_record.delete()
        return redirect('medical_record_list', student_id=student.id)
    return render(request, 'medical_record_confirm_delete.html', {'medical_record': medical_record, 'student': student})
