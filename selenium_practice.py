from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3) # 기다리기

driver.get('http://naver.com')

elem = driver.find_element_by_id('query')
elem.send_keys('블로그맛집')

# 확인 or enter 키 누르기
elem.submit()
# elem.send_keys(Keys.ENTER)

'''
find_element_by_name('HTML_name')
find_element_by_id('HTML_id')
find_element_by_xpath('/html/body/some/xpath')
find_element_by_css_selector('#css > div.selector')
find_element_by_class_name('some_class_name')
find_element_by_tag_name('h1')
'''

# class <- menu

elem = driver.find_element_by_class_name('tab')
elem.click


html = driver.page_source
print(html)