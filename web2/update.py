#!/user/local/bin/python3
print('Content-Type: text/hhtml')
print()
import cgi, os

files = os.listdir('data')
print(files)
listStr = ''
for item in files:
    listStr = listStr + '<li><a href=index.py?id={name}>{name}</a></li>'.format(name=item)
print(listStr)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value 
    description = open('data/'+pageId, 'r').read() # r을 생략하면 r 기본값으로 read
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    
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
          <form action="process_update.py">
              <input type="hidden" name="pageId" value="{form_default_title}">
              <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
              <p><textarea rows="4" name="desrciption" placeholder="desrciption">{form_default_description}</textarea></p>
              <p><input type="submit"></p>
          </form>
      </body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, form_default_title=pageId, form_default_description=description))