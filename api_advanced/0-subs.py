import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    return 0
