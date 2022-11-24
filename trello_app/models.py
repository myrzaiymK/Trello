import datetime
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


# class Favourites(models.Mo )


class Board(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    favourites = models.ManyToManyField(User, related_name="favourites", blank=True)
    archive = models.ManyToManyField(User, related_name="archive", blank=True)

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


class Comment(models.Model):
    body = models.TextField(max_length=300)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey('Card', blank=True, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.card)


#
#
# class CheckList(models.Model):
#     title = models.CharField(max_length=100)
#
#
# class Label(models.Model):
#     title = models.CharField(max_length=30)




