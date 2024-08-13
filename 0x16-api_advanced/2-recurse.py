#!/usr/bin/python3
"""
Use Api to get all post
"""

import requests


def recurse(subreddit, hot_list=[]):
    """get all hot post"""
    if after is None:
        return []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    url += f"?limit=100&after={after}"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    rjson = response.json()
    hot_posts_json = rjson.get("data").get("children")
    return hot_list = recurse(subreddit, [], rjson.get("data").get("after"))
