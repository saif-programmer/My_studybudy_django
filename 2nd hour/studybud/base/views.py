import os
from django.shortcuts import render, redirect
from pendulum import instance
from .models import Room
from .forms import RoomForm
#from django.http import HttpResponse


# rooms=[
#     {'id':1, 'name':"Lets learn Django"},
#     {'id':2, 'name':"I love FASTAPI"},
#     {'id':3, 'name':"NoSQL is Amazing"},
# ]

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context) #os.path.join('base', 'home.html')

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)  # os.path.join('base', 'room.html) 

def createRoom(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        room = RoomForm(request.POST, instance=room)
        if room.is_valid():
            room.save()
            return redirect('home') 

    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})