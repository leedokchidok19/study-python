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
          <p>
              <iframe width="1280" height="720" src="https://www.youtube.com/embed/7T7r_oSp0SE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
              </iframe>
          </p>
          <a href="create.py">create</a>
          {update_link}
          {delete_action}
          <h2>{title}</h2>
          <p>
              {desc}
          </p>
          <!--댓글 기능 disqus 사용-->
            <div id="disqus_thread"></div>
                <script>

                /**
                *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
                *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
                /*
                var disqus_config = function () {
                this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
                this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
                };
                */
                (function() { // DON'T EDIT BELOW THIS LINE
                var d = document, s = d.createElement('script');
                s.src = 'https://web1-2.disqus.com/embed.js';
                s.setAttribute('data-timestamp', +new Date());
                (d.head || d.body).appendChild(s);
                })();
                </script>
                <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
            <!--댓글 기능-->
            <!--Start of Tawk.to Script-->
                <script type="text/javascript">
                var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
                (function(){
                var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
                s1.async=true;
                s1.src='https://embed.tawk.to/57a72994c11fe69b0bd8fa90/default';
                s1.charset='UTF-8';
                s1.setAttribute('crossorigin','*');
                s0.parentNode.insertBefore(s1,s0);
                })();
                </script>
            <!--End of Tawk.to Script-->
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