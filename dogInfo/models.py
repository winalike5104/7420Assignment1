from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100,default = " ")
    sex = models.CharField(max_length=100)
    description = models.TextField(null=True)
    data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

    def snippet(self):
        return self.description[:50] +'...'



class Appointments(models.Model):
    id = models.AutoField(primary_key=True,)
    activity = models.CharField(max_length=50,default = " " )
    time = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    suburb = models.CharField(max_length=50)
    author = models.ManyToManyField(User)
    # ['time','address','status','city','suburb','author']


class DogAppointments(models.Model):
    name =  models.CharField(max_length=50)
    appointment = models.ForeignKey(Appointments,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    