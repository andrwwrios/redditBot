#!/usr/bin/env python
# coding: utf-8

# In[26]:


# access reddit api to make bot posts
import praw
get_ipython().run_line_magic('run', 'reddit_keys.py')
reddit = praw.Reddit(
    username=username, password=password,
    client_id=client_id, client_secret=client_secret,
    user_agent="a custom python script for user /" + str(username)
)

# import time to access real time and sleep
import time


# In[ ]:


def redditPostsSchedule():
    currentDay = time.localtime().tm_wday  # Get the current day (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    currentTime = time.localtime().tm_hour * 100 + time.localtime().tm_min  # Get the current time in military format
    
    if currentDay == 0:  # Monday
        if currentTime == 900:
            reddit.subreddit('myBotPostsForClass').submit('Monday🤒', selftext='gm to all.')  
        elif currentTime == 2300:
            reddit.subreddit('myBotPostsForClass').submit('gn', selftext='')  
    elif 1 <= currentDay <= 3:  # Tuesday to Thursday
        if currentTime == 900:
            reddit.subreddit('myBotPostsForClass').submit('Good morning :)', selftext='I love tuesdays') 
        elif currentTime == 2300:
            reddit.subreddit('myBotPostsForClass').submit('goodnight :)', selftext='sweet dreams!')  
    elif currentDay == 4:  # Friday
        if currentTime == 900:
            reddit.subreddit('myBotPostsForClass').submit("Friday!🎉", selftext='Cant wait for the weekend') 
        elif currentTime == 2300:
            reddit.subreddit('myBotPostsForClass').submit("Let's party!", selftext='Message me for the address😉') 
    elif currentDay == 5:  # Saturday
        if currentTime == 1300:
            reddit.subreddit('myBotPostsForClass').submit('goodd morrning', selftext='Last night was crazy') 
        elif currentTime == 2359:
            reddit.subreddit('myBotPostsForClass').submit('goodnight', selftext='') 
    elif currentDay == 6:  # Sunday
        if currentTime == 2300:
            reddit.subreddit('myBotPostsForClass').submit('Goodnight, time for the cycle to repeat...', selftext='')

# Loop to continuously check and post according to the schedule
while True:
    redditPostsSchedule()
    time.sleep(60)  # Check every minute (adjust as needed)

