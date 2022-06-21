from django.urls import path
from django.http import HttpResponse
from . import views

app_name = "rooms"

urlpatterns = [path("list/", views.ListRoomsView.as_view())]
