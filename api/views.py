from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import LoginInfo
from .serializers import LoginInfo, LoginInfoSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST']) # with out decorators  we can not use post
def loginInfo_list(request):

    if request.method == 'GET':
        loginInfo = LoginInfo.objects.all()
        serializer = LoginInfoSerializer(loginInfo,many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
       
        serializer = LoginInfoSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def loginInfo_detail(request,pk):
    try:
        loginInfo = LoginInfo.objects.get(pk=pk)
    except LoginInfo.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        
        serializer = LoginInfoSerializer(loginInfo)
        return Response(serializer.data)

    elif request.method == 'PUT':

        
        serializer = LoginInfoSerializer(loginInfo,data = request.data)

        if serializer.is_valid():

            serializer.save()
            return  Response(serializer.data)

        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':

        loginInfo.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        