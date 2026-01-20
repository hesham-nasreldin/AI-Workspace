from django.shortcuts import render, redirect
from notes import models as notes
from todolist import models as todolist
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    return render(request, "authentication/index.html")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("my-login")

    context = {"registerform": form}

    return render(request, "authentication/register.html", context=context)


def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")
    context = {"loginform": form}

    return render(request, "authentication/my-login.html", context=context)


@login_required(login_url="my-login")
def dashboard(request):
    recent_todos = todolist.TodoList.objects.filter(user=request.user, completed=False).order_by("-created_at")
    recent_notes = notes.Notes.objects.filter(user=request.user).order_by("-created_at")
    context = {
        "recent_todos": recent_todos[:10],
        "recent_notes": recent_notes[:10],
        "recent_todos_count": recent_todos.count(),
        "recent_notes_count": recent_notes.count(),
    }
    return render(request, "authentication/dashboard.html", context=context)


def user_logout(request):
    auth.logout(request)

    return redirect("")

