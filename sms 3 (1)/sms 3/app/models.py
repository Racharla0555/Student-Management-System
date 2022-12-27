from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    hall=models.CharField(max_length=10)
    section=models.CharField(max_length=10)
    batch=models.CharField(max_length=30)
    year=models.CharField(max_length=20)
    sem=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class itStudent(models.Model):
    name=models.CharField(max_length=40)
    hall=models.CharField(max_length=10)
    section=models.CharField(max_length=10)
    batch=models.CharField(max_length=30)
    year=models.CharField(max_length=20)
    sem=models.CharField(max_length=30)
    def __str__(self):
        return self.name
branch_choice=(('IT','IT'),("CSE","CSE"),("CS","CS"),("DS","DS"),("ECE","ECE"),("CIV","CIV"))
section_choice=(('A','A'),('B','B'),('C','C'))
from datetime import date
# Create your models here.
class iStudent(models.Model):
    student_name=models.CharField(max_length=30)
    hall_ticket=models.CharField(max_length=20)
    branch=models.CharField(max_length=10,choices=branch_choice,default='IT')
    section=models.CharField(max_length=2,choices=section_choice,default='B')
    date_of_birth=models.DateField(default=date.today())
    father_name=models.CharField(max_length=30)
    mother_name=models.CharField(max_length=30)
    parent_number=models.DecimalField(max_digits=10,decimal_places=0)
    student_number=models.DecimalField(max_digits=10,decimal_places=0)
    address=models.CharField(max_length=100)
    attendence=models.DecimalField(max_digits=5,decimal_places=2)
    CGPA=models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.student_name
