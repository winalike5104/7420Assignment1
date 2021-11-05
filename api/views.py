from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import Article, ArticleSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt # with out decorators  we can not use post
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return JsonResponse(serializer.data,safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)