import os, html_sanitizer
# from html_sanitizer import Sanitizer
sanitizer = html_sanitizer.Sanitizer()

def getList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        listStr = listStr + '<li><a href=index.py?id={name}>{name}</a></li>'.format(name=item)
    return listStr