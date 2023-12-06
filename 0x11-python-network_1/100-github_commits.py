#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    repoName = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repoName, owner)

    response = requests.get(url)
    commits = response.json()
    for i in range(10):
        try:
            print("{}: {}".format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')
                ))
        except IndexError:
            pass
