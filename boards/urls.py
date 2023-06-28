from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_board),
    path("all_board/", views.show_all_board),
    path("board_reviews/", views.show_board_reviews)

    # path("/all", views.all_board),
    # path("<int:board_id>/<str:board_content>", views.make_board)
]