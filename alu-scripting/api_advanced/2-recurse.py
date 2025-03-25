import requests

def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None if len(hot_list) == 0 else hot_list
    data = response.json().get('data', {})
    hot_list.extend([post.get('data', {}).get('title') for post in data.get('children', [])])
    new_after = data.get('after')
    return recurse(subreddit, hot_list, new_after) if new_after else hot_list
