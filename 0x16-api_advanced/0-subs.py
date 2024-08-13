#!/usr/bin/python3
"""Importing a module to make requests"""
import requests


def number_of_subscribers(subreddit):
    """Function to determine the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User-Agent for educational purpose'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
        except Exception as e:
            return 0
