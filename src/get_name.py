from selenium import webdriver
import chromedriver_binary
import time
import csv

def get():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://stocks.finance.yahoo.co.jp/us/ranking/?kd=4&tm=d')

    name_list = []
    st_class = driver.find_element_by_class_name('dsRanking_body')
    dt = st_class.find_elements_by_tag_name('dt')
    for data in dt:
        a_tag = data.find_elements_by_tag_name('a')
        for a in a_tag:
            #print(a.find_element_by_tag_name('strong').text)
            name = a.find_element_by_tag_name('strong').text
            name_list.append(name)

    driver.quit()
    print(name_list)

    with open('data/sample.csv', 'w') as f:
        f.writelines('\n'.join(name_list))