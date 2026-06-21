from django.urls import path
from . import views
urlpatterns = [
    path("", view=views.index_sell, name="index_sell")
]
