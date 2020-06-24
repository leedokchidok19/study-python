#!/user/local/bin/python3

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title =  form["title"].value
description =  form["description"].value

opened_file = open('data/'+pageId, 'w')
opened_file.write(description)
opened_file.close()

# os.rename(현재 파일 이름, 바꿀 파일 이름)
os.rename('data/'+pageId, 'data/'+title)

# Redirection
print('Location: index.py?id='+title)
print()