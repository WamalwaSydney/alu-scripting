import requests

def count_words(subreddit, word_list, counts={}, after=None, is_initial=True):
    if is_initial:
        counts.clear()
        word_list = [word.lower() for word in word_list]
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200 and is_initial:
        return
    elif response.status_code == 200:
        data = response.json().get('data', {})
        for post in data.get('children', []):
            title = post.get('data', {}).get('title', '').lower()
            for word in word_list:
                counts[word] = counts.get(word, 0) + title.split().count(word)
        new_after = data.get('after')
        if new_after:
            count_words(subreddit, word_list, counts, new_after, False)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
