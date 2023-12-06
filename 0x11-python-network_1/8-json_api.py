#!/usr/bin/python3
"""
This Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) >= 2:
        parameter = {"q": sys.argv[1]}
    else:
        parameter = {"q": ""}

    response = requests.post(url, data=parameter)

    try:
        r = response.json()

        if not r:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
