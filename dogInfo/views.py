from django import forms
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def dogInfo_list(request):
    if request.user:
        dog_list = Dog.objects.filter(author = request.user).order_by('data')
        return render(request, 'dogInfo.html',{'dog_list':dog_list})
    else:
        return render(request,'/login/')

def dog_detail(request,slug):
    dog = Dog.objects.get(name = slug)
    
    return render(request,'dog_detail.html',{'dog':dog})

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



 