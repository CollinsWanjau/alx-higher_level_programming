#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST
request to the passed URL with email as paremeter
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    req = sys.argv[1]
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    url = urllib.request.Request(req, data.encode("ascii"))
    with urllib.request.urlopen(url) as response:
        print(response.read().decode("utf-8"))
