#!/usr/bin/env python3
import urllib.request
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    utf8_content = the_page.decode('utf-8')
print(f"Body response:")
print(f"\t- type: {type(the_page)}")
print(f"\t- content: {the_page}")
print(f"\t- utf8 content: {utf8_content}")
