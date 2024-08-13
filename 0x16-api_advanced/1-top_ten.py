#!/usr/bin/python3
"""Use reddit api to get posts"""

import requests


def top_ten(subreddit):
    """get 10 hot post"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get("data").get("children")
    topies = "\n".join(post.get("data").get("title") for post in data)
    print(topies)
