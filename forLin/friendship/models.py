from django.db import models
from users.models import User
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver


class Friendship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='friendship')
    friends = models.ManyToManyField('self', symmetrical=True)

    def __str__(self):
        return self.user.first_name

class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friedship_requests')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_friedship_requests')
    is_approved = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.from_user)

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        instance.friendship = Friendship.objects.create(user=instance)
    instance.friendship.save()