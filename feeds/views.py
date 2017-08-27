# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserTweet, TwitterUser
from django.utils import timezone
from datetime import date
from django.core.urlresolvers import resolve
from django.template import RequestContext,loader
import re

# from .import settings
# Create your views here.
from twython import Twython

from tweetfeds import settings
from . import cron_task 
import requests
import pprint
import json
import twitter

def login_page(request):
    return render(request,'feeds/login_page.html')

def login_twitter(request):
    # twitter_ = Twython(settings.APP_KEY, settings.APP_SECRET)
    # auth = twitter_.get_authentication_tokens(callback_url='/thanks')
    # file = open('temp_token','w')
    # OAUTH_TOKEN = auth['oauth_token']
    # OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    # file.write(OAUTH_TOKEN+"\n")
    # file.write(OAUTH_TOKEN_SECRET)
    # file.close()

    # return redirect(auth['auth_url'])
    return redirect('/thanks')

def thanks(request):
    # file = open('temp_token','r')
    # profile = []
    # for line in file:
    #     profile.append(line)
    # # profile_tokens = [e.oauth_token for e in TwitterUser.objects.all()]
    # # profile_secrets = [e.oauth_secret for e in TwitterUser.objects.all()]
    # print ("profile",profile[0])
    # OAUTH_TOKEN = profile[0]
    # OAUTH_TOKEN_SECRET = profile[1]
    # print ("TOKEN and SECRET",OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    # oauth_verifier = request.GET['oauth_verifier']

    # twitter_ = Twython(settings.APP_KEY, settings.APP_SECRET,
    #               OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    # final_step = twitter_.get_authorized_tokens(oauth_verifier)
    # FINAL_OAUTH_TOKEN = final_step['oauth_token']
    # FINAL_OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
    # twitter_ = Twython(settings.APP_KEY,settings.APP_SECRET,FINAL_OAUTH_TOKEN,FINAL_OAUTH_TOKEN_SECRET)
    
    # new_twitter = twitter.Api(settings.APP_KEY, settings.APP_SECRET, FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET,sleep_on_rate_limit=True) #shifting api for advanced access

    # user = twitter_.verify_credentials()
    # data = json.dumps(twitter_.get_home_timeline())
    # l_data = json.loads(data)

    # check_user = TwitterUser.objects.filter(user_id = user['id'])
    # user_found = 1
    # try:
    #     pro_token_data = TwitterUser.objects.get(user_id = user['id'])
    #     pro_token_data = {
    #         'oauth_token':pro_token_data.oauth_token,
    #         'oauth_token_secret':pro_token_data.oauth_token_secret
    #     }
    # except:
    #     user_found = 0
    # # print ("Pro token",pro_token_data['oauth_token'])
    # print "Count of check_user",check_user.count()
    
    # if check_user.count() == 0 or user_found:
    #     user_profile = TwitterUser()
    #     if not user_found:
    #         user_profile.user_id = user['id'] #change user id if no user found
    #         user_profile.user_name = user['screen_name']
    #         user_profile.oauth_token = FINAL_OAUTH_TOKEN
    #         user_profile.oauth_secret = FINAL_OAUTH_TOKEN_SECRET
    #         print ("SEE THIS",user['id'],user['screen_name'])
    #         user_profile.save()
            
            
    #         for i in range(len(l_data)):
    #             user_tweets = UserTweet()
    #             # user_tweets.json_data = l_data
    #             user_tweets.since_id = l_data[i]['id']
    #             user_tweets.user_id_id = user['id']
            
    #             user_tweets.created_at = l_data[i]['created_at']
    #             user_tweets.favorite_count = l_data[i]['favorite_count']
    #             user_tweets.text = l_data[i]['text']
            
    #             urls = l_data[i]['entities']['urls']
    #             url_s = ''
    #             if urls:
    #                 url_s+=urls[0]['url'] 
    #             for u in range(1,len(urls)):
    #                 try:
    #                     url_s = url_s+','+urls[u]['url']
    #                 except Exception as err:
    #                     print ("Exception while getting urls fix please",err)
    #             print ('URLS',url_s)
    #             user_tweets.urls = url_s
    #             user_tweets.screen_name_tweet = l_data[i]['user']['screen_name']
    #             user_tweets.save()

    #         try:
    #             cron_task.createThread(twitter_,user['id'])
    #         except:
    #             print ("Error in creating cron_task")
    #     else:
    #         if pro_token_data['oauth_token']!=FINAL_OAUTH_TOKEN and pro_token_data['oauth_secret']!=FINAL_OAUTH_TOKEN_SECRET:
    #             user_profile.oauth_secret = FINAL_OAUTH_TOKEN_SECRET
    #             user_profile.oauth_token = FINAL_OAUTH_TOKEN
    #             user_profile.save()
    #             try:
    #                 cron_task.createThread(twitter_,user['id'])
    #             except:
    #                 print ("Error in creating cron_task")
    
    # # return HttpResponse('<h5>thanks '+user['screen_name']+' for signing up!</h5>')
    # request.session['user_name'] = user['screen_name']
    # request.session['user_id']=user['id']
    request.session['user_name'] = 'm_s_e_m_n'
    request.session['user_id'] = 864336222784593920
    return redirect('/feeder')

def feeder(request):
    name_user = request.session['user_name']
    id_user = request.session['user_id']
    message = ''
    if request.method == 'GET' and request.GET.get('start_date'):
        date = request.GET.get('start_date')
        year,month,day = date.split('-')
        tweets = UserTweet.objects.filter(user_id_id=id_user,year=year,month=month,day=day)
        if not tweets:
            return HttpResponse('<h3>No tweets found for '+str(day)+'/'+str(month)+'/'+str(year)+'</h3>')
        message = 'Tweets for '+str(day)+'/'+str(month)+'/'+str(year)
    else:
        tweets = UserTweet.objects.filter(user_id_id = id_user)[:30]
        message = 'Showing recent tweets'
    # data_ = UserTweet.objects.all()
    
    # for e in data:
    #     print e.text
    context = {}
    user_info = {
        'user_name':name_user
    }
    # print data;
    # context['user_name'] = name_of_user
    key = 1
    for tweet in tweets:
        tweet_content = {}
        tweet_content['text'] = re.sub(r'http\S+', '',tweet.text)
        tweet_content['urls'] = tweet.urls.split(',')
        tweet_content['favorite'] = tweet.favorite_count
        tweet_content['tweet_by'] = tweet.screen_name_tweet
        tweet_content['retweet_count'] = tweet.retweet_count
        tweet_content['created_at'] = tweet.created_at
        context[str(key)] = tweet_content
        key+=1
    context['user'] = name_user
    context['message'] = message
    # loader.get_template('login_page.html')
    # print ("CONTEXT",context)
    # print (type(context))
    return render(request,'feeds/feeder.html',{'contexts':context})

