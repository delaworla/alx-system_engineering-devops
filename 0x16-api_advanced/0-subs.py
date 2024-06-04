#!/usr/bin/python3

"""
A function that queries the Reddit API and returns the number of subscribers 
(not active users, total subscribers) for a given subreddit. 
If an invalid subreddit is given, the function should return 0.

"""

import requests

def number_of_reddit_subscribers(subreddit):
    sub_request = requests.get