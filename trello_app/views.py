from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Column
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .models import Board
from .forms import BoardForm
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render
from .models import Board, Card
from .forms import BoardForm, ColumnForm, CardForm




def archive_post(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if board.archive.filter(pk=request.user.id).exists():
        board.archive.remove(request.user)
    else:
        board.archive.add(request.user)
    return redirect(reverse("board_detail", kwargs={"pk": board.id}))


def archive_list(request):
    user = request.user
    archive_posts = user.archive.all()
    context = {

        'archive_posts': archive_posts,
    }
    return render(request, 'board/archive.html', context)


def create_card(request):
    context = {}

    form = CardForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return redirect('/home/board/')

    context['form'] = form
    return render(request, "board/create_view.html", context)


def card_delete(request, pk, template_name='card/card_delete.html'):
    contact = get_object_or_404(Card, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('/')
    return render(request, template_name, {'object':contact})



def card_detail(request, pk):
    card = Card.objects.get(pk=pk)
    context = {
        'card': card,

    }
    return render(request, 'card/card_detail.html', context)


def create_column(request):
    context = {}

    form = ColumnForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "board/create_view.html", context)


def column_delete(request, pk, template_name='column/column_delete.html'):
    contact = get_object_or_404(Column, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('/home/doards/')
    return render(request, template_name, {'object':contact})


def create_view(request):
    context = {}

    form = BoardForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "board/create_view.html", context)



def delete(request, pk, template_name='board/board_delete.html'):
    board = get_object_or_404(Board, pk=pk)
    if request.method=='POST':
        board.delete()
        return redirect('/home/boards/')
    return render(request, template_name, {'object':board})



def board_index(request):
    boards = Board.objects.all()
    user = request.user
    archive_posts = user.archive.all()
    # context = {
    #
    #     'archive_posts': archive_posts,
    # }
    # board = Board.archive.filter(pk=request.user.id)

    # is_archive = False

    # for board in boards:
    #
    #     if board.archive.filter(pk=request.user.id).exists():


    context = {
        'boards': boards,
        'archive_posts': archive_posts,

        # 'board_pk': board,

    }
    return render(request, 'board/board_index.html', context)


def board_detail(request, pk):
    board = Board.objects.get(pk=pk)
    boards = Board.objects.all()
    is_favourite = False
    if board.favourites.filter(pk=request.user.id).exists():
        is_favourite = True


    is_archive = False

    if board.archive.filter(pk=request.user.id).exists():
        is_archive = True

    context = {
        'board': board,
        'boards': boards,
        'is_favourite': is_favourite,
        'is_archive': is_archive,
    }
    return render(request, 'board/board_detail.html', context)



def favourite_post(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if board.favourites.filter(pk=request.user.id).exists():
        board.favourites.remove(request.user)
    else:
        board.favourites.add(request.user)
    return redirect(reverse("board_detail", kwargs={"pk": board.id}))


def favourite_list(request):
    user = request.user
    favourite_posts = user.favourites.all()
    context = {

        'favourite_posts': favourite_posts,
    }
    return render (request, 'board/favorites.html', context)



def test_board(request):
    return render(request, 'board/boards.html')

