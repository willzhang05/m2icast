#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re

r = requests.get('https://routerproxy.bldc.net.internet2.edu/routerproxy')
html = BeautifulSoup(r.text, 'html.parser')
devices = str(html.find(id='Core Routers'))
out=re.findall(r'value=".{8,}"', devices)
out=sorted([re.sub(r'[^.\d]', '', o) for o in out])
