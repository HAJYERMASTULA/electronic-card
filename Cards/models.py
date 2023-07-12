from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User



class Course(models.Model):
    course_name = models.CharField(max_length=20)
    faculty = models.CharField(max_length=50)
    course_code = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    def __str__(self):
        return self.course_name


class Student(models.Model):
    GENDER_OPTIONS=[
        ("M", "Male"),
        ("F","Female"),
    ]
    MARITAL_STATUS_OPTIONS=[
        ("M","Married"),
        ("S","Single"),

    ]
    SESSION_OPTIONS = [
        ("Day","Day"),
       ("Evening", "Evening"),
        ("Weekend", "Weekend"),
    ]
    student_name = models.CharField(max_length = 50, null= True, blank= True)
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    session = models.CharField(max_length = 8, choices = SESSION_OPTIONS ,null= True, blank= True)
    date_of_birth = models.DateField(auto_now = False)
    address = models.CharField(max_length = 25, null= True, blank= True)
    religion = models.CharField(max_length=20)
    telephone_no = models.CharField(max_length = 15)
    nationality = models.CharField(max_length = 20,null= True, blank= True)
    marital_status = models.CharField(max_length=2, choices= MARITAL_STATUS_OPTIONS)
    def __str__(self):
        return self.student_name

class FeesStructure(models.Model):
    SEMESTER = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
    ]
    YEAR = [
        ("1", "1yr"),
        ("2", "2yr"),
        ("3", "3yr"),
        ("4", "4yr"),
    ]
    academic_year = models.CharField(max_length= 10)
    year_of_study = models.CharField(max_length = 3, choices = YEAR)
    semester = models.CharField(max_length = 3, choices = SEMESTER)
    functional_fees = models.IntegerField(null = True, blank = True)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    def __int__(self):
        return self.course
    


class TuitionPayment(models.Model):
    fees_structure = models.ForeignKey(FeesStructure, on_delete = models.CASCADE)
    amount_paid = models.IntegerField(null = True, blank = True)
    payment_date = models.DateField(auto_now = False)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    def __str__(self):
        return self.student

class Card(models.Model):
    STATUS = [
        ("Active","Active"),
        ("De-activated", "Deactivated"),
        ("Terminated", "Terminated")
    ]
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    cardno =models.CharField(max_length=12, default="",unique=True)
    barcode = models.ImageField(upload_to='barcodes/',blank=True)
    status = models.CharField(max_length = 15, choices = STATUS)
    def __str__(self): 
        return self.status
    
    def save(self,*args,**kwargs):
        EAN = barcode.get_barcode_class('ean13')
        buffer = BytesIO()
        ean = EAN(f'{self.cardno}{self.student}{self.status}', writer=ImageWriter())
        ean.write(buffer)
        self.barcode.save(f'{self.cardno}.png',File(buffer), save=False)
        return super().save(*args, **kwargs)


class Clearance(models.Model):

    SEMESTER = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
    ]
    YEAR = [
        ("1", "1yr"),
        ("2", "2yr"),
        ("3", "3yr"),
        ("4", "4yr"),
    ]
    card = models.ForeignKey(Card, on_delete = models.CASCADE)
    year_of_study = models.CharField(max_length = 3, choices=YEAR)
    semester = models.CharField(max_length = 2, choices=SEMESTER)
    academic_year = models.CharField(max_length = 10)
    is_test_cleared = models.BooleanField(default = False)
    is_exam_cleared = models.BooleanField(default = False)
    is_library_cleared = models.BooleanField(default = False)
    def __str__(self):
        return self.year_of_study


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
# class YourModel(models.Model):
#     field_name = models.CharField(max_length=100)
#     students_name = models.ForeignKey(Student, on_delete = models.CASCADE)

