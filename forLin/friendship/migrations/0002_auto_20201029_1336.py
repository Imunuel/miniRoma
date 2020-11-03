# Generated by Django 3.0.4 on 2020-10-29 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201029_1336'),
        ('friendship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='friends',
            field=models.ManyToManyField(related_name='_friendship_friends_+', to='friendship.Friendship'),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Friendship', to='users.User'),
        ),
    ]
