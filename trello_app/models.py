import datetime
from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='new/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.title


class Column(models.Model):
    title = models.CharField(max_length=30, blank=True)
    board = models.ForeignKey('Board', related_name='column', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Card(models.Model):
    column = models.ForeignKey('Column', related_name='card', blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    # members = models.ManyToManyField('User', blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
#
#
# class Comments(models.Model):
#     comment = models.TextField(max_length=300)
#     author = models.ForeignKey(User, blank=True)
#     date = models.DateField(default=datetime.date.today)
#     card = models.ForeignKey(Card, blank=True)
#
#
# class CheckList(models.Model):
#     title = models.CharField(max_length=100)
#
#
# class Label(models.Model):
#     title = models.CharField(max_length=30)




