#!/user/local/bin/python3
'''
함수 사용 전
권한 없음 오류
sudo chmod a+x 파일명.py
'''
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
    desrciption = open('data/'+pageId, 'r').read() # r을 생략하면 r 기본값으로 read
    update_link = '<a href="update.py?id="{}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    desrciption = 'Hello, web'
    update_link = ''
    delete_action = ''
    
print('''<!doctype html>
<html>
      <head>
          <title>WEB - Welcome</title>
          <meta charset="utf-8">
      </head>
      <body>
          <h1><a href="index.py">WEB</a></h1>
          <ol>
              {listStr}
          </ol>
          <a href="create.py">create</a>
          {update_link}
          {delete_action}
          <h2>{title}</h2>
          <p>{desc}
          </p>
      </body>
</html>
'''.format(title=pageId, desc=desrciption, listStr=listStr, update_link=update_link, delete_action=delete_action))
