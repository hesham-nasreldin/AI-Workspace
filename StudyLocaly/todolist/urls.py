from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_todolist, name="todos_page"),
    path("edit/<int:todo_id>", views.edit_todo, name="edit_todo"),
    path("completed-tasks/", views.completed_todos, name="completed-tasks")
]
