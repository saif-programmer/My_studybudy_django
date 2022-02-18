import os
from django.shortcuts import render
#from django.http import HttpResponse


rooms=[
    {'id':1, 'name':"Lets learn Django"},
    {'id':2, 'name':"I love FASTAPI"},
    {'id':3, 'name':"NoSQL is Amazing"},
]

# Create your views here.
def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context) #os.path.join('base', 'home.html')

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'base/room.html', context)  # os.path.join('base', 'room.html) 