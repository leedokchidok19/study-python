import selenium    # pip install selenium
from selenium import webdriver

search_term = '검색대상'
url = f'https://www.google.co.in/search?q={search_term}&tbm=isch'

browser = webdriver.Chrome('chromedriver.exe')
browser.get(url)

for i in range(200):
    browser.execute_script('window.scrollBy(0,10000)')

for idx, el in enumerate(browser.find_elements_by_class_name('rg_ic')):
    el.screenshot(str(idx) + '.png')

browser.close()
