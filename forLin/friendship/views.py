from django.shortcuts import render
from .models import Friendship, FriendshipRequest
from django.views.generic import ListView, DetailView

class FriendsPage(ListView):
    model = Friendship
    template_name = 'friendship/fri.html'
    context_object_name = 'fri' 

    def get_context_data(self, **kwards):
        ctx = super(FriendsPage, self).get_context_data(**kwards)
        
        ctx['friend'] = Friendship.objects.filter(id='2')
        return ctx

