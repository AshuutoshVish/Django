#Structure of the Database
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    dob = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['name']
