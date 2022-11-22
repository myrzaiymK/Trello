from django.shortcuts import render, redirect
from .models import Board, Column
from django.urls import reverse


# Create your views here.


from django.shortcuts import render

# relative import of forms
from .models import Board
from .forms import BoardForm
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render

# relative import of forms
from .models import Board, Card
from .forms import BoardForm, ColumnForm, CardForm


def create_card(request):
    context = {}

    form = CardForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "board/create_view.html", context)



def card_detail(request, pk):
    card = Card.objects.get(pk=pk)
    columns = list(card.column.all())
    context = {
        'card': card,

    }
    return render(request, 'board/board_detail.html', context)


def create_column(request):
    context = {}

    form = ColumnForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "board/create_view.html", context)



def create_view(request):
    context = {}

    form = BoardForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "board/create_view.html", context)




def board_index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'board/board_index.html', context)


def board_detail(request, pk):
    board = Board.objects.get(pk=pk)
    column = Column.objects.get(pk=pk)
    columns = list(board.column.all())
    cards = list(column.card.all())
    context = {
        'board': board,
        'columns': columns,
        'cards': cards

    }
    return render(request, 'board/board_detail.html', context)


def test_board(request):
    return render(request, 'board/boards.html')

