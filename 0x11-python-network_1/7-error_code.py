#!/usr/bin/python3
"""
This Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
import sys
import requests

if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    if request.status_code < 400:
        print(request.text)
    else:
        print("Error code:", request.status_code)
