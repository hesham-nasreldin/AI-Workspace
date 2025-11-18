from django.shortcuts import render, HttpResponse

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            print("good")

    return render(request, "authentication/register.html")