#!/usr/bin/python3
"""
import
"""

import requests


def top_ten(subreddit):
    # URL for the Reddit API to get the hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid any issues
    headers = {'User-Agent': 'Custom User Agent'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Extract and print the titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])
        except KeyError:
            # Invalid subreddit or unexpected JSON structure
            print(None)
    else:
        # Invalid subreddit or other API error
        print(None)


# Test the function
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
