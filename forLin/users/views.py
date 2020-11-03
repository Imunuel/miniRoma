from django.shortcuts import render
from .models import User 
from friendship.models import Friendship, FriendshipRequest
from django.views.generic import ListView, DetailView

class HomePage(ListView):
    model = User
    template_name = 'users/home.html'
    context_object_name = 'users' 
