#!/user/local/bin/python3
# print('Content-Type: text/hhtml')
# print()
import cgi
form = cgi.FieldStorage()

title =  form["title"].value 
description =  form["description"].value

# print(title, description) print가 있으면 중간의 Header값이 변경된다.
opened_file = open('data/'+title, 'w')
opened_file.write(description)

# Redirection - Location: 뒤에오는 곳으로 이동
print('Location: index.py?id='+title)
print()