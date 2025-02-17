from django.db import models

class Application(models.Model):
    # Define status choices
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    # Fields for the Application model
    application_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    application_date = models.DateField(auto_now_add=True)  # Automatically set to current date when created
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Application {self.application_id} - {self.student_name}"


class Payment(models.Model):
    # Define payment method choices
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Online Payment', 'Online Payment'),
    ]

    # Fields for the Payment model
    payment_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateField(auto_now_add=True)  # Automatically set to current date when created
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.amount}"


class Document(models.Model):
    # Define document type choices
    DOCUMENT_TYPE_CHOICES = [
        ('Birth Certificate', 'Birth Certificate'),
        ('Transcript', 'Transcript'),
        ('Other', 'Other'),
    ]

    # Fields for the Document model
    document_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPE_CHOICES)
    document_file = models.BinaryField()  # BYTEA in PostgreSQL is equivalent to BinaryField in Django

    def __str__(self):
        return f"Document {self.document_id} - {self.document_type}"
from django.db import models

class Student(models.Model):
    # Define gender choices
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    # Fields for the Student model
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"Student {self.student_id} - {self.student_name}"


class Contact(models.Model):
    # Define contact relationship choices
    RELATIONSHIP_CHOICES = [
        ('Parent', 'Parent'),
        ('Guardian', 'Guardian'),
        ('Emergency Contact', 'Emergency Contact'),
    ]

    # Fields for the Contact model
    contact_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='contacts')
    contact_name = models.CharField(max_length=100)
    contact_relationship = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.CharField(max_length=100)

    def __str__(self):
        return f"Contact {self.contact_id} - {self.contact_name}"


class MedicalRecord(models.Model):
    # Fields for the MedicalRecord model
    medical_record_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='medical_records')
    medical_condition = models.CharField(max_length=100)
    allergy_alert = models.CharField(max_length=100)

    def __str__(self):
        return f"Medical Record {self.medical_record_id} - {self.medical_condition}"


class StudentPhoto(models.Model):
    # Fields for the StudentPhoto model
    student_photo_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='photos')
    photo_file = models.BinaryField()

    def __str__(self):
        return f"Photo {self.student_photo_id} - {self.student.student_name}"


class Attendance(models.Model):
    # Define attendance status choices
    ATTENDANCE_STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    # Fields for the Attendance model
    attendance_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    attendance_date = models.DateField(auto_now_add=True)
    attendance_status = models.CharField(max_length=10, choices=ATTENDANCE_STATUS_CHOICES)

    def __str__(self):
        return f"Attendance {self.attendance_id} - {self.student.student_name}"


class AttendanceReport(models.Model):
    # Define attendance status choices
    ATTENDANCE_STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    # Fields for the AttendanceReport model
    attendance_report_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_reports')
    report_date = models.DateField(auto_now_add=True)
    attendance_status = models.CharField(max_length=10, choices=ATTENDANCE_STATUS_CHOICES)

    def __str__(self):
        return f"Attendance Report {self.attendance_report_id} - {self.student.student_name}"


class Fee(models.Model):
    # Define fee type choices
    FEE_TYPE_CHOICES = [
        ('Tuition', 'Tuition'),
        ('Registration', 'Registration'),
        ('Other', 'Other'),
    ]

    # Fields for the Fee model
    fee_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees')
    fee_type = models.CharField(max_length=50, choices=FEE_TYPE_CHOICES)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return f"Fee {self.fee_id} - {self.fee_type}"


class Invoice(models.Model):
    # Fields for the Invoice model
    invoice_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='invoices')
    invoice_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.invoice_id} - {self.student.student_name}"


class Payments(models.Model):
    # Define payment method choices
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Online Payment', 'Online Payment'),
    ]

    # Fields for the Payment model
    payment_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.amount}"


class Expense(models.Model):
    # Define expense type choices
    EXPENSE_TYPE_CHOICES = [
        ('Salaries', 'Salaries'),
        ('Utilities', 'Utilities'),
        ('Other', 'Other'),
    ]

    # Fields for the Expense model
    expense_id = models.AutoField(primary_key=True)
    expense_type = models.CharField(max_length=50, choices=EXPENSE_TYPE_CHOICES)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Expense {self.expense_id} - {self.expense_type}"
