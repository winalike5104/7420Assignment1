from django import forms
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def dogInfo_list(request):
    if request.user:
        dog_list1 = Dog.objects.filter(author = request.user).order_by('data')
        dog_list2 = Dog.objects.filter().exclude(author = request.user)
        return render(request, 'dogInfo.html',{'dog_list1':dog_list1,'dog_list2':dog_list2})
    else:
        return render(request,'/login/')

def dog_detail(request,slug,judge):
    dog = Dog.objects.get(name = slug)
    if judge == 'yes':
        judge = 1
    else:
        judge = 0
    return render(request,'dog_detail.html',{'dog':dog,'judge':judge})

@login_required(login_url="/login/")
def dog_post(request):
    if request.method == 'POST':
        form = forms.RegisterDog(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/dogInfo_list/')
    else:
        form = forms.RegisterDog()
    return render(request,'dog_post.html',{'form':form})

@login_required(login_url="/login/")
def appointments(request):
    if request.user:
        print('it is here')
        appointments_list1 = []
        appointments_list2 = []
        for i in Appointments.objects.all():
            if request.user in i.author.all():
                appointments_list1.append(i)
            else:
                appointments_list2.append(i)

        
        # create a appointments_list1 for own
        # create a appointments_list2 for others
        
        print(appointments_list2)
        return render(request, 'appointments.html',
            {'appointments_list1':appointments_list1,
            'appointments_list2':appointments_list2,
            "form":0})
    else:
        return render(request,'/login/')

def setAappointment(request):
    if request.method == 'POST':
        form = forms.AppointmentsForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.author.add(request.user)
            
            return redirect('/appointments/')
    else:
        form = forms.AppointmentsForm()
    return render(request,'appointments.html',{'form':form})

def appointment_detail(request,slug,judge):
    print(judge)
    if judge == 'yes':
        judge = 1
    else:
        judge = 0
    appointment = Appointments.objects.get(id = slug)
    print(appointment.author.all())
    lst = []
    
    for i in appointment.author.all():
        lst.append(i.username)
    return render(request,'appointment_detail.html',{'appointment':appointment,'lst':lst,'judge':judge})
    
def book(request,id):
    print(request.user)
    appointment = Appointments.objects.get(id = id)
    appointment.author.add(request.user)
    return redirect('/appointments/')

def quit(request,id):
    appointment = Appointments.objects.get(id = id)
    appointment.author.remove(request.user)
    return redirect('/appointments/')



def editdog(request,id):
    thisDog = Dog.objects.get(id = id);
    if request.method == 'POST':
        form = forms.RegisterDog(request.POST,request.FILES)
        if form.is_valid():
            thisDog.name = form.cleaned_data['name']
            thisDog.birthday = form.cleaned_data['birthday']
            thisDog.sex = form.cleaned_data['sex']
            thisDog.description = form.cleaned_data['description']
            thisDog.save()
            return redirect('/dogInfo_list/')
    else:
        form = forms.RegisterDog()
    return render(request,'dog_edit.html',{'form':form,"id":id})

'''
id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.IntegerField(null=True)
    sex = models.CharField(max_length=100)
    description = models.TextField(null=True)
    data = models.DateTimeField(auto_now_add=True)
'''

 