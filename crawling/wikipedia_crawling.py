#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup # pip install bs4
from urllib.request import urlopen

# response = urlopen('https://en.wikipedia.org/wiki/Main_Page')
with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('a'):
        print(anchor.get('href', '/'))

'''
https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)
'''