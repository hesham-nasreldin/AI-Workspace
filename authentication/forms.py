from django.contrib.auth.models import User

def register(username:str, password:str):
    new_user = User.objects.create_user(username=username, password=password)
    new_user.save()
