from django.db import models

# Create your models here.
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
    course = models.CharField(max_length=20,null=False)
    session = models.CharField(max_length = 8, choices = SESSION_OPTIONS ,null= True, blank= True)
    date_of_birth = models.DateField(auto_now = False)
    address = models.CharField(max_length = 25, null= True, blank= True)
    religion = models.CharField(max_length=20)
    telephone_no = models.CharField(max_length = 15)
    nationality = models.CharField(max_length = 20,null= True, blank= True)
    marital_status = models.CharField(max_length=2, choices= MARITAL_STATUS_OPTIONS)
    def __str__(self):
        return self.student_name

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
        return self.cardno
    
'''
def save(self,*args,**kwargs):
        EAN = barcode.get_barcode_class('ean13')
        buffer = BytesIO()
        ean = EAN(f'{self.cardno}{self.student}{self.status}', writer=ImageWriter())
        ean.write(buffer)
        self.barcode.save(f'{self.cardno}.png{self.student}{self.status}',File(buffer), save=False)
        return super().save(*args, **kwargs)    
        '''