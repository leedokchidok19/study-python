#!/user/local/bin/python3

import cgi, os
form = cgi.FieldStorage()
pageId =  form["pageId"].value

os.remove('data/'+pageId)

# Redirection
print('Location: index.py)
print()
      
# sudo chmod
# sudo chmod a+x process_delete.py 