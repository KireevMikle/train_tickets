from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()


class Train(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

class Seat(models.Model):
    number = models.IntegerField()
    train = models.ForeignKey(Train, on_delete=models.CASCADE)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

