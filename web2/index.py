#!/user/local/bin/python3
print('Content-Type: text/hhtml')
print()
import cgi, os, view, html_sanitizer
# from html_sanitizer import Sanitizer
sanitizer = html_sanitizer.Sanitizer()
# sanitizer.sanitize('css내용')

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value 
    desrciption = open('data/'+pageId, 'r').read() # r을 생략하면 r 기본값으로 read
    # desrciption = desrciption.replace('<', '&lt;') # XSS 방지
    # desrciption = desrciption.replace('>', '&gt;') # XSS 방지
    desrciption = sanitizer.sanitize(desrciption) # XSS 방지
    title = sanitizer.sanitize(title)
    update_link = '<a href="update.py?id="{}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    title = pageId = 'Welcome'
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
'''.format(
    title=title,
    desc=desrciption,
    listStr=view.getList(),
    update_link=update_link,
    delete_action=delete_action)
     )

# 참고 생활코딩 : https://www.youtube.com/watch?v=11AudAjpvSw