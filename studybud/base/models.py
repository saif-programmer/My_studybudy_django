from email.policy import default
from django.db import models
# from django.contrib.auth.models import User we will customize our user model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # if the topic is deleted the room will not
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # null --> must be description      blank --> for form user can sumbit room without description
    #
    participants = models.ManyToManyField(User, related_name="participant", blank=True)
    #
    updated = models.DateTimeField(auto_now=True) # will has value every time it is sumbitted
    created = models.DateTimeField(auto_now_add=True) # will save one value at the initiating of it   
    
    class Meta: # to order the Rooms
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # (user)one TO many(messages)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # when delete Room all messages will be deleted because of CASCADE
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # will has value every time it is sumbitted
    created = models.DateTimeField(auto_now_add=True) # will save one value at the initiating of it

    class Meta: # to order the Messages
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50] # the first 50 character