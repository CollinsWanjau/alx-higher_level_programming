#!/usr/bin/env python3
"""
The script fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as \
                response:
        the_page = response.read()
        print(f"Body response:")
        print(f"\t- type: {type(the_page)}")
        print(f"\t- content: {the_page}")
        print(f"\t- utf8 content: {the_page.decode('utf-8')}")
