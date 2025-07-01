from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'dob', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter age'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        }
        labels = {
            'name': 'Full Name',
            'age': 'Age',
            'dob': 'Date of Birth',
            'email': 'Email Address',
        }
