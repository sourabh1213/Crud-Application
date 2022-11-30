from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import User
from .models import StudentRegistration

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = User(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            reg = StudentRegistration(name=nm, email=em)
            reg.save()
            fm = User()
    else:
        fm = User()
    stud = StudentRegistration.objects.all()
    return render(request, 'enroll/home.html', {'form':fm, 'stu':stud})

def delete_data(request, id):
    if request.method == 'POST':
        min = StudentRegistration.objects.get(pk=id)
        min.delete()

def update(request, id):
    if request.method == 'POST':
        edt= StudentRegistration.objects.get(pk=id)
        fm = User(request.POST, instance=edt)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Updated Successfully')
    else:
        edt = StudentRegistration.objects.get(pk=id)
        fm = User(instance=edt)
    return render(request, 'enroll/update.html', {'form':fm})