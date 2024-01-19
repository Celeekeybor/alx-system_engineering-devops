#!/usr/bin/python3
"""import request"""

import requests

def count_words(subreddit, word_list, word_counts={}, after=None):
    # Base case: if after is None, there are no more pages of results
    if after is None:
        # Sort the word counts in descending order by count and then alphabetically
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_counts:
            print(f"{word.lower()}: {count}")
        return

    # URL for the Reddit API to get the hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    # Set a custom User-Agent to avoid any issues
    headers = {'User-Agent': 'Custom User Agent'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Extract and parse the titles of the hot posts
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                # Split the title into words
                words = title.split()
                # Count occurrences of each word in word_list
                for word in word_list:
                    if word in words:
                        # Update the count for the word
                        if word in word_counts:
                            word_counts[word] += words.count(word)
                        else:
                            word_counts[word] = words.count(word)
            # Recursively call the function with the 'after' parameter for pagination
            count_words(subreddit, word_list, word_counts, data['data']['after'])
        except KeyError:
            # Invalid subreddit or unexpected JSON structure
            return
    else:
        # Invalid subreddit or other API error
        return

# Test the function
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [x for x in sys.argv[2].split()]
        count_words(subreddit, keywords)
