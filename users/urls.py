from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserList.as_view(), name='users_home')
]
