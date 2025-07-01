from django.shortcuts import render, redirect
from .models import Employee
from django import forms

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    position = forms.CharField(max_length=50)
    salary = forms.DecimalField(decimal_places=2)
    email = forms.EmailField()


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list.html', {'employees': employees})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            Employee(**form.cleaned_data).save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/form.html', {'form': form})


def employee_update(request, pk):
    emp = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                setattr(emp, key, value)
            emp.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(initial=emp.to_mongo().to_dict())
    return render(request, 'employee/form.html', {'form': form})


def employee_delete(request, pk):
    emp = Employee.objects.get(id=pk)
    if request.method == 'POST':
        emp.delete()
        return redirect('employee_list')
    return render(request, 'employee/confirm_delete.html', {'employee': emp})
