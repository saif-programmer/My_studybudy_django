from django.forms import ModelForm
from .models import Room, User
# from django.contrib.auth.models import User we wil use our user model
from django.contrib.auth.forms import UserCreationForm # create user


class MyUserCreationForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ["name", "username", "email", "password1", "password2"]

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # will containe every attributes of the data like topic and host and description
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [ "avatar", 'name','username', "email", "bio"] 
