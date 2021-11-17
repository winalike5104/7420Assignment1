from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def log_in(request):
    return render(request, 'login/login.html')

def jump_to_register_page(request):
    print("to here")
    return render(request, 'login/register.html')

def jump_to_index(request):
    return render(request, 'login/index.html')
