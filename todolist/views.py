from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from auth.forms import CreateUserForm

# Create your views here.
print(CreateUserForm.Meta.model())


@login_required(login_url="my-login")
def index_todolist(request):
    if request.method == "POST":

        if "add" in request.POST:
            print("add")

            todo = request.POST.get("todo")
            TodoList.objects.create(todo=todo, user=request.user)

            for item in TodoList.objects.filter(user=request.user):
                print(item.todo)

            return redirect("home_page")

        if "delete" in request.POST:
            todo_id = request.POST.get("delete")
            print(todo_id)
            todo = get_object_or_404(TodoList, id=todo_id, user=request.user)
            todo.delete()

        if "done" in request.POST:
            todo_id = request.POST.get("done")
            todo = get_object_or_404(TodoList, id=todo_id, user=request.user)
            todo.completed = True
            todo.save()

            print(f"Todo :{todo.completed}\n")

            return redirect("home_page")
    context = {
        "todos": TodoList.objects.filter(user=request.user)
    }

    return render(request, template_name="todolist/index.html", context=context)


@login_required(login_url="my-login")
def edit_todo(request, todo_id):
    todo_item = get_object_or_404(TodoList, id=todo_id, user=request.user)
    context = {
        "todo_id": todo_id,
        "todo": todo_item,
    }
    if "done" in request.POST:
        print("done")
        new_todo = request.POST.get("new_todo")

        todos = get_object_or_404(TodoList, id=todo_id)
        todos.todo = new_todo

        todos.save()

        return redirect("home_page")
    return render(request, template_name="todolist/edit.html", context=context)


@login_required(login_url="my-login")
def completed_todos(request):
    todos = TodoList.objects.filter(user=request.user, completed=True)
    all_todos = [todo for todo in todos]
    if request.method == "POST":

        if "undo" in request.POST:
            print("undo")
            undo_button_id = request.POST.get("undo")
            print(f"Undo button data: {undo_button_id}")
            todo = get_object_or_404(TodoList, id=undo_button_id)
            todo.completed = False
            todo.save()

            return redirect("completed-tasks")

    return render(request, "todolist/completed_todos.html", context={"all_todos": all_todos})
