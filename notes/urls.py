from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="notes_index"),
    path("edit_notes/<int:note_id>", views.edit_note, name="edit_notes"),
]
