#!/usr/bin/python3
"""Importing a module to make requests"""
import requests


def number_of_subscribers(subreddit):
    """Function to determine the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User-Agent for educational purpose'}
    response = requests.get(url, headers=headers allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get(subscribers)
