from django.shortcuts import render

# Create your views here.

def index_sell(request):
    return render(request, "sell/index.html")