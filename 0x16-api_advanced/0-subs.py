#!/usr/bin/python3

"""
Import
"""
import requests


def number_of_subscribers(subreddit):
    # URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid any issues
    headers = {'User-Agent': 'Custom User Agent'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Extract the number of subscribers
            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError:
            # Invalid subreddit or unexpected JSON structure
            return 0
    else:
        # Invalid subreddit or other API error
        return 0


# Test the function
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
