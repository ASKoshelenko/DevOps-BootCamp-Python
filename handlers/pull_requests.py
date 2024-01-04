
import os

TOKEN = os.getenv("TOKEN")
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def get_pull_requests(state):
    """
    Example of return:
    [
        {"title": "Add useful stuff", "num": 56, "link": "https://github.com/boto/boto3/pull/56"},
        {"title": "Fix something", "num": 57, "link": "https://github.com/boto/boto3/pull/57"},
    ]
    """

    # Write your code here

    return []
