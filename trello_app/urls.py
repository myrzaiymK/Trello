from django.urls import path
from .views import board_detail, board_index, test_board, create_view, create_column, create_card

urlpatterns = [
    path('', board_index),
    path('board', test_board, name='boards'),
    path('boards/', board_index, name='board_index'),
    path('board/<int:pk>/', board_detail, name="board_detail"),
    path("board/add/", create_view, name="board-add"),
    path("column/add/", create_column, name="column-add"),
    path("card/add/", create_card, name="card-add"),

]
