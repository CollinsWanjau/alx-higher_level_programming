#!/usr/bin/env python3
"""
The script fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(f"Body response:")
        print(f"\t- type: {type(the_page)}")
        print(f"\t- content: {the_page}")
        print(f"\t- utf8 content: {the_page.decode('utf-8')}")
