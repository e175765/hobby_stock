from selenium import webdriver
import chromedriver_binary
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get('https://stocks.finance.yahoo.co.jp/us/ranking/?kd=4&tm=d')
#all_st = driver.find_elements_by_class_name('dsMarket isMain marB10')
#print(all_st)
#add line

#st_class = driver.find_element_by_class_name('dsRanking_list.marB10')
st_class = driver.find_element_by_class_name('dsRanking_body')
com_name = st_class.find_elements_by_tag_name('a')
st_ratio = st_class.find_elements_by_class_name('ratio.textRight')
count = 0
sum = 0
for i, com in enumerate(com_name):
    if i % 2 == 0:
        print('name : {0}'.format(com.text))
        print('ratio : {0}'.format(st_ratio[count].text))
        hoge = st_ratio[count].text
        index = hoge.find('%')
        #print(hoge[0:index])
        #print(hoge)
        if len(hoge[1:index]) > 0:
            if hoge[0] == '+':
                sum += float(hoge[1:index])
            elif hoge[0] == '-':
                sum -= float(hoge[1:index])
        else:
            #hoge.replace('-', '0')
            #sum += float(hoge[0:index])
            pass
        count += 1
    else :
        pass

print(sum)
#for tag in tag_a:
#    name = tag.find_element_by_tag_name('a')
#    print(tag.text)

#for cl in cl_name:
#    print(cl.text)
#cl_name = st_class.find_elements_by_class_name('name')
#cl_name2 = cl_name[0].find_elements_by_tag_name('a')
#print(cl_name[0].text)
#print(cl.text)
#st_val = driver.find_elements_by_class_name('dsMarket_meta')
#for i in st_val:
#    print(i.text)
driver.quit()
