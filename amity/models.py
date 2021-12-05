from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=40)
    enrollment = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    email = models.EmailField()


from django.db import models

class Block(models.Model):
    dish_name = models.CharField(max_length=40)
    price = models.CharField(max_length=40)
    image = models.FileField()

