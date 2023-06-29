from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("<int:user_id>", views.UserDetail.as_view())
]
