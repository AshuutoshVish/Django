from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits.")

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(15), MaxValueValidator(100)])
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    enrolled_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.course_name}"

    class Meta:
        ordering = ['-enrolled_on']
