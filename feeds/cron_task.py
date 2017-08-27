import thread
import time
import json

from .models import UserTweet

def do(thread_name, delay, twitter):
    
    while(True):
        time.sleep(delay)
        try:
            id_of_user = int(thread_name)
            all_data = UserTweet.objects.filter(user_id_id=id_of_user)
            # print ("ALL DATA",all_data)
            since_id = max([e.since_id for e in all_data])
            print ('since_id', since_id)
            # data = twitter.GetHomeTimeline(since_id=since_id)
            data = twitter.get_home_timeline(since_id=since_id)
            if data:
                data = json.dumps(data)
                l_data = json.loads(data)
            # since_id = l_data[0]['id']
                # table.since_id = since_id
                # table.user_id_id = id_of_user
                # user_tweets.json_data = data
                print ("NO OF TWEETS",len(l_data))
                for i in range(len(l_data)):
                    user_tweets = UserTweet()
                    user_tweets.since_id = l_data[i]['id']
                    user_tweets.user_id_id = id_of_user
                
                    user_tweets.created_at = l_data[i]['created_at']
                    user_tweets.favorite_count = l_data[i]['favorite_count']
                    user_tweets.text = l_data[i]['text']
                
                    urls = l_data[i]['entities']['urls']
                    url_s = ''
                    if urls:
                        url_s+=urls[0]['url'] 
                    for u in range(1,len(urls)):
                        try:
                            url_s = url_s+','+urls[u]['url']
                        except Exception as err:
                            print ("Exception while getting urls fix please",err)
                    print ('URLS',url_s)
                    
                    user_tweets.urls = url_s
                    user_tweets.screen_name_tweet = l_data[i]['user']['screen_name']
                    user_tweets.save()
                    # table.save()
        except Exception as err:
            print err
            # print ("Error in syncing UserTweet for ",user_id)

def createThread(twitter,user_id):
    try:
        thread.start_new_thread(do,(str(user_id),100,twitter))
    except:
        print ("Error in creating thread")
        