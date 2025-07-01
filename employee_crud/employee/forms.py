from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'position', 'salary', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter age'}),
            'position': forms.TextInput(attrs={'placeholder': 'Enter position'}),
            'salary': forms.NumberInput(attrs={'placeholder': 'Enter salary'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        }
        labels = {
            'name': 'Full Name',
            'age': 'Age',
            'position': 'Position',
            'salary': 'Salary',
            'email': 'Email Address',
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Employee.objects(email=email).first():
            raise forms.ValidationError("This email already exists.")
        return email
