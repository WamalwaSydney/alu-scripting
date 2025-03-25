import requests

def top_ten(subreddit):
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        for post in response.json().get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    else:
        print(None)
