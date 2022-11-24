from django.contrib import admin
from .models import Board, Column, Card, Comment

# Register your models here.

admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Card)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'author', 'created_on', 'card']
    list_filter = ['created_on']
