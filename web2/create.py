#!/user/local/bin/python3
print('Content-Type: text/hhtml')
print()
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value 
    desrciption = open('data/'+pageId, 'r').read() # r을 생략하면 r 기본값으로 read
else:
    pageId = 'Welcome'
    desrciption = 'Hello, web'
    
print('''<!doctype html>
<html>
      <head>
          <title>WEB - Welcome</title>
          <meta charset="utf-8">
      </head>
      <body>
          <h1><a href="index.html">WEB</a></h1>
          <ol>
              {listStr}
          </ol>
          <a href="create.py">create</a>
          <form action="process_create.py">
              <p><input type="text" name="title" placeholder="title"></p>
              <p><textarea rows="4" name="desrciption" placeholder="desrciption"></textarea></p>
              <p><input type="submit"></p>
          </form>
      </body>
</html>
'''.format(title=pageId, desc=desrciption, listStr=view.getList())