from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from .models import CreateUserForm
from .accountForm import checkForm, resetForm 
from django.contrib.auth.models import User
import random
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def signup_view(request):
    
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/dogInfo_list/')
    else:
        form = CreateUserForm()
    return render (request,'signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            # return redirect('/dogInfo_list/')
            user = form.get_user()
            login(request,user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/dogInfo_list/')
    else:
        form = AuthenticationForm()
    return render(request,"login.html",{'form':form})

def logout_view(request):
    if request.method == 'POST':
        if request.user:
            logout(request)
        return redirect('/login/')


def sendEmail(request,username,code):
    email = EmailMessage(
        'Verification',
        'Verification Code :'+code,
        settings.EMAIL_HOST_USER,
        [username]

    )
    email.fail_silently = False
    email.send()
    form = resetForm()
    return render(request,"reset.html",{'form':form})

def check(request):
    if request.method == 'POST':
        form = checkForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username = form.cleaned_data['userName']):
                account = User.objects.filter(username = form.cleaned_data['userName'])
                lst = [str(random.randint(0,9)) for i in range(6)]
                codeString = ''.join(lst)
                request.session['username'] = account[0].username
                request.session['varifycode'] = codeString
                email = EmailMessage(
                'Verification',
                'Verification Code :'+codeString,
                settings.EMAIL_HOST_USER,
                [account[0].email]

                )
                email.fail_silently = False
                email.send()
                form = resetForm()
                email = account[0].email
                crypto = []
                for i in range(0,len(email)):
                    if i < 4 or i > len(email)-5:
                        crypto.append(email[i])
                    else:
                        crypto.append('*')
                cryptoString = ''.join(crypto)
                return render(request,"reset.html",{'form':form,'message':cryptoString})

            else:
                
                return render(request,"check.html",{'form':form,'message':'this userName does not exist'})
                
        else:
            return HttpResponse('it is not in here')
    else:
        form = checkForm()
    return render(request,"check.html",{'form':form,'message':0})

def reset(request):
    if request.method == 'POST':
        form = resetForm(request.POST)
        code = request.session.get('varifycode')#request.session.get ('_auth_user_id') 
        username = request.session.get('username')
        if form.is_valid():
            if code != form.cleaned_data['verify_code']:
                return render(request,"reset.html",{'form':form,'message':0})
            else:
                useraccount = User.objects.get(username = username)
                newpass= form.cleaned_data['newPassword']
                print(newpass)
                useraccount.set_password(newpass)
                useraccount.save()
                return redirect('/login/')
    else:
        form = resetForm()
    return render(request,"reset.html",{'form':form,'message':0})



'''
if request.method == 'POST':
        form = forms.RegisterDog(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/dogInfo_list/')
'''