#!/usr/bin/python3
"""Recursively get all hot posts for a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot posts for a subreddit."""
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return None if not hot_list else hot_list
    data = response.json().get('data', {})
    hot_list.extend([post.get('data', {}).get('title') for post in data.get('children', [])])
    new_after = data.get('after')
    return recurse(subreddit, hot_list, new_after) if new_after else hot_list


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
