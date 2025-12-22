from django.urls import path
from . import views

urlpatterns = [
    path("", views.notes_index, name="notes_index"),
    path("edit/<int:note_id>", views.edit_note, name="edit_notes"),
]
