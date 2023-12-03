#!/usr/bin/python3
"""
This Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
using the requests package
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers["x-request-id"])
