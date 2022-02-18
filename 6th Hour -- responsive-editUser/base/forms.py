from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # will containe every attributes of the data like topic and host and description
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', "email"] 
