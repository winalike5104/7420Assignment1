from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def log_in(request):
    return render(request, 'login/index.html')
