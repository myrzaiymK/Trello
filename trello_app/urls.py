from django.urls import path, re_path
from .views import board_detail, board_index, test_board, create_view, create_column, create_card, card_detail, delete, column_delete, card_delete, favourite_post, favourite_list, archive_post, archive_list

urlpatterns = [
    path('', board_index),
    path('board', test_board, name='boards'),
    path('boards/', board_index, name='board_index'),
    path('board/<int:pk>/', board_detail, name="board_detail"),
    path("board/add/", create_view, name="board-add"),
    path("board/<int:pk>/delete/", delete, name="delete_board"),
    path("column/add/", create_column, name="column-add"),
    path("card/add/", create_card, name="card-add"),
    path("card/<int:pk>/", card_detail, name="card-detail"),
    path('delete/<int:pk>', column_delete, name='column_delete'),
    path('card/<int:pk>/delete/', card_delete, name='card_delete'),
    path('<int:pk>/favourite_post/', favourite_post, name='favourite_post'),
    path("boards/favourites/", favourite_list, name="favourite_list"),
    path('<int:pk>/archive_post/', archive_post, name='archive_post'),
    path("boards/archive/", archive_list, name="archive_list"),
]
