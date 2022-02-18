from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # if the topic is deleted the room will not
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # null --> must be description      blank --> for form user can sumbit room without description
    #participant =
    updated = models.DateTimeField(auto_now=True) # will has value every time it is sumbitted
    created = models.DateTimeField(auto_now_add=True) # will save one value at the initiating of it   
    
    class Meta: # to order the Rooms
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # (user)one TO many(messages)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # when delete Room all messages eill be deleted because of CASCADE
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # will has value every time it is sumbitted
    created = models.DateTimeField(auto_now_add=True) # will save one value at the initiating of it   
    def __str__(self):
        return self.body[0:50] # the first 50 character