# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class TwitterUser(models.Model):
    user_id = models.IntegerField(primary_key = True)
    oauth_secret = models.CharField(max_length=100)
    oauth_token = models.CharField(max_length=100)
    user_name = models.CharField(max_length=25)


class UserTweet(models.Model):
    user_id = models.ForeignKey(TwitterUser)
    since_id = models.IntegerField()
    # json_data = models.TextField()
    
    year = models.IntegerField(default=timezone.datetime.now().year)
    month = models.IntegerField(default=timezone.datetime.now().month)
    day = models.IntegerField(default=timezone.datetime.now().day)
    
    urls = models.CharField(max_length = 100,default='')
    text = models.CharField(max_length = 170,default='')
    created_at = models.CharField(max_length = 70,default='')
    
    retweet_count = models.IntegerField(default=0)
    screen_name_tweet = models.CharField(max_length=25,default='unknown')
    favorite_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'UserTweet'
        ordering = ['-since_id']


    # time = models.DateTimeField(default = timezone.now())
    
# class TwitterProfile(models.Model):
#     """
#         An example Profile model that handles storing the oauth_token and
#         oauth_secret in relation to a user. Adapt this if you have a current
#         setup, there's really nothing special going on here.
#     """
#     user = models.OneToOneField(User)
#     oauth_token = models.CharField(max_length=200)
#     oauth_secret = models.CharField(max_length=200)
