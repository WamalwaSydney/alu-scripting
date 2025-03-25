#!/usr/bin/python3
"""Module to count and print occurrences of keywords in hot posts."""

import requests


def count_words(subreddit, word_list, counts=None, after=None, is_initial=True):
    """Counts and prints keyword occurrences in hot posts.
    
    Args:
        subreddit (str): The subreddit to query.
        word_list (list): Keywords to count.
        counts (dict): Accumulator for keyword counts.
        after (str): Pagination token.
        is_initial (bool): Flag for initial call.
    """
    if counts is None:
        counts = {}
    if is_initial:
        word_list = [word.lower() for word in word_list]
        counts.clear()
    
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        if is_initial:
            return
        else:
            return
    
    data = response.json().get('data', {})
    for post in data.get('children', []):
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            counts[word] = counts.get(word, 0) + title.split().count(word)
    
    new_after = data.get('after')
    if new_after:
        count_words(subreddit, word_list, counts, new_after, False)
    elif is_initial:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
