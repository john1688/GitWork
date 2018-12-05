
from selenium import webdriver
from string import Template
import time
import random



def attention_data():
    i=1
    b =webdriver.Chrome()
    b.maximize_window()
    b.get("https://blog.csdn.net/nav/newarticles")
    while i < 100:
        try:
            i = i + 1
            m = str(i)
            path = "/html/body/div[2]/div/main/ul/li[" + m + "]/div/div[1]/h2/a"
            url = b.find_element_by_xpath(path).get_attribute("href")
            urlData = url.replace('article/details/', 'phoenix/article/digg?ArticleId=')
            with open('c:\\testZan.txt', 'a') as zanData:
                zanData.write(urlData)
                zanData.write('\n')
        except:
            js = "var q=document.documentElement.scrollTop=10000"
            b.execute_script(js)
            time.sleep(3)
            continue

def attention_admire():
    i = 80
    b = webdriver.Chrome()
    b.maximize_window()
    b.get("https://passport.csdn.net/passport_fe/login.html")
    b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
    b.find_element_by_id("all").send_keys("")
    time.sleep(3)
    b.find_element_by_id("password-number").send_keys("")
    time.sleep(3)
    b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button").click()
    time.sleep(3)
    while i > 1:
        i = i - 1
        try:
            for line in open('c:\\testZan.txt', 'r'):
                line = line[:-1]
                str = line
                time.sleep(1.7)
                b.get(str)
        except:
            continue

for i in range(1,100):
    i=i+1
    attention_data()
    attention_admire()

