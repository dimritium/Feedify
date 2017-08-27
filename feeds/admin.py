# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserTweet, TwitterUser 
# Register your models here.
# admin.site.register(UsersInfo)
admin.site.register(UserTweet)
admin.site.register(TwitterUser)