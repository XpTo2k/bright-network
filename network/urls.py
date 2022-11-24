
from django.urls import path

from . import views

urlpatterns = [
    # RENDER URLS
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_idea", views.new_idea, name="new_idea"),
    path("user/<str:user>", views.user, name="user"),
    path("following", views.following, name="following"),
    path("ideas", views.ideas, name="ideas"),

    # API URLS
    path("idea/<int:id>", views.idea, name="idea"),
    path("edit_idea", views.edit_idea, name="edit_idea"),
    path("get_user/<int:id>", views.get_user, name="get_user"),
]
