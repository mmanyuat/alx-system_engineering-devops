#!/usr/bin/python3
"""Importing a module to make requests"""
import requests


def number_of_subscribers(subreddit):
    """Function to determine the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-reddit-app/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
