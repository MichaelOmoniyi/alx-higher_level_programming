#!/usr/bin/python3
""" A script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    urls = [
            "https://alx-intranet.hbtn.io/status",
            "https://intranet.hbtn.io/status",
            "http://0.0.0.0:5050/status"
            ]
    for url in urls:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            html = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(html)))
            print("\t- content: {}".format(html))
            print("\t- utf8 content: {}".format(html.decode("utf-8")))
