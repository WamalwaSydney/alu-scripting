#!/usr/bin/python3
"""Print the titles of the top 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Print the top 10 hot posts for a subreddit."""
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code == 200:
        for post in response.json().get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    else:
        print(None)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
