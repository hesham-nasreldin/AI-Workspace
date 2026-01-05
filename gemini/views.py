from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from google import genai
import environ
import os

# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
# environ.Env.read_env(os.path.join(BASE_DIR, 'ai_Assistant/.env'))

environ.Env.read_env()
# API_KEY = env("GEMINI_API_KEY")
API_KEY = "my api key  "

messages = {}


def answer(user_text):
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(model="gemini-2.0-flash", contents=f"{user_text}")
    return response.text


@login_required(login_url="my-login")
def home_page(request):
    global messages

    if request.method == "POST":
        message = request.POST.get("message")

        if "send" in request.POST:
            messages[message] = answer(message)
            print(messages)

    return render(
        request,
        template_name="gemini/index.html",
        context={
            "messages": messages,
        }
    )
