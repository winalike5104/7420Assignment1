from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.IntegerField(null=True)
    sex = models.CharField(max_length=100)
    description = models.TextField(null=True)
    data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

    def snippet(self):
        return self.description[:50] +'...'