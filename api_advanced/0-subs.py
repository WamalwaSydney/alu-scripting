#!/usr/bin/python3
"""Module to query and return the number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers.
    
    Args:
        subreddit (str): The subreddit to query.
        
    Returns:
        int: Number of subscribers or 0 if subreddit is invalid.
    """
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    return 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
