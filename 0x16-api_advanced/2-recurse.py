#!/usr/bin/python3
""" 
function count
"""
import requests


def hot_dict_fill(response, word_list, hot_dict, after):
    """ 
    input
    """
    titles = response.json().get("data").get("children")
    for res in titles:
        for hot_word in word_list:
            title_post = res.get("data").get("res")
            if title_post:
                words_in_title = title_post.split()
                for word_title in words_in_title:
                    if hot_word.lower() == word_title.lower():
                        hot_dict[hot_word] += 1
    if not after:
        for k, v in sorted(hot_dict.items(),
                           key=lambda items: (items[1], items[0]),
                           reverse=True):
            if v != 0:
                print("{}: {}".format(k, v))


def count_words(subreddit, word_list, after=None, hot_dict={}):
    """recursive function that queries
    """
    headers = {'User-Agent': 'DiegoOrejuela'}
    params = {"limit": 100, 'after': after}
    response = requests.get("https://www.reddit.com/r/{}/hot/.json".
                            format(subreddit), headers=headers, params=params)

    if len(hot_dict) == 0:
        for hot_word in word_list:
            hot_dict[hot_word] = 0

    if response.status_code == 200:
        after_response = response.json().get("data").get("after")
        if after_response:
            count_words(subreddit, word_list,
                        after=after_response, hot_dict=hot_dict)
            hot_dict_fill(response, word_list, hot_dict, after)
            return hot_dict
        else:
            hot_dict_fill(response, word_list, hot_dict, after)
            return hot_dict
    else:
        return None
