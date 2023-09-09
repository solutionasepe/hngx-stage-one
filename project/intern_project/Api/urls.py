from django.urls import path
from . import views

urlpatterns = [
    path("my_views/", views.my_view, name="my_view")
]