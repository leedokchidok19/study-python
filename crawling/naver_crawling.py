#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup # pip install bs4
from urllib.request import urlopen

# response = urlopen('https://www.naver.com/')
with urlopen('https://www.naver.com/') as response:
    soup = BeautifulSoup(response, 'html.parser')
    i = 1
    f = open('새파일.txt', 'w')
    for anchor in soup.select('span.ah_k'):
        # print(anchor)
        #print(str(i)+'위 : '+anchor.get_text())
        data = str(i)+'위 : '+anchor.get_text()+'\n'
        i = i + 1
        f.write(data)
    f.close()

'''
https://www.naver.com/
python write text file
https://beomi.github.io/gb-crawling/posts/2017-02-27-HowToMakeWebCrawler-With-Selenium.
selenium  : pip install selenium
https://hoony-gunputer.tistory.com/48
조코딩 : https://velog.io/@joygoround/%EC%A1%B0%EC%BD%94%EB%94%A9-%EC%99%84%EC%84%B1%ED%98%95-%EC%84%9C%EB%B9%84%EC%8A%A4-%EB%A7%8C%EB%93%A4%EA%B8%B0-1
'''