from django.urls import path
from . import views


urlpatterns = [
    path('', views.FriendsPage.as_view(), name='friends'),
]