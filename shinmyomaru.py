# coding: UTF-8

import chromedriver_binary
import re
from datetime import datetime

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://shinmyomaru.com/category/tyouka')
browser.find_elements_by_class_name('readmore')[0].click()
results = []
for i in range(10):
    element_title = browser.find_element_by_class_name('entry-title')
    element_content = browser.find_element_by_class_name('entry-content')
    results.append(element_content.text)
    browser.find_element_by_class_name('previous').click()

for result in results:
    if 'マゴチ船' in result:
        searched_magochi = re.search(r'\d*〜\d*(?=本)', result)
        searched_date = re.search(r'\d\d?月\d\d?日', result)

        date_result = datetime.strptime(
            '2020年' + searched_date[0], '%Y年%m月%d日').date()
        min_result_magochi, max_result_magochi = searched_magochi.group(0).split('〜')[
            :2]

        print(date_result)
        print('min: ' + min_result_magochi)
        print('max: ' + max_result_magochi)
