from django.urls import path
from . import views

urlpatterns = [
    path("", views.CommentList.as_view(), name='comments_home')
]
