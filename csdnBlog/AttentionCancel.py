
from selenium import webdriver
from string import Template
import time
import random
import requests
#微信版
def attention_weixin():
	i=84720
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
	b.get("https://i.csdn.net/#/uc/follow-list")
	time.sleep(2)
	while i > 1:
		i = i - 1
		js = "var q=document.documentElement.scrollTop=100000"
		b.execute_script(js)
		time.sleep(1)
		b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]").click()
		time.sleep(1)
		# time.sleep(1)
		for n in range(1, 12):
			n = n + 1
			b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[4]").click()
			time.sleep(2)
			for m in range(12, 19):
				m = m + 1
				m = str(m)
				b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[" + m + "]/a[3]").click()
				time.sleep(2)



#采集自己的粉丝数据
def attention_fan():
	b = webdriver.Chrome()
	b.maximize_window()
	b.get("https://passport.csdn.net/passport_fe/login.html")
	b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
	b.find_element_by_id("all").send_keys("")
	time.sleep(3)
	b.find_element_by_id("password-number").send_keys("Ma__900531900")
	time.sleep(3)
	b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button").click()
	time.sleep(3)
	b.get("https://i.csdn.net/#/uc/fan-list")
	time.sleep(3)
	totalList=b.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]').text
	#b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]").click()
	totalList=int(totalList)
	while totalList >0 :
		try:
			totalList=str(totalList)
			datalistPath = '/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[' + totalList + ']'
			b.find_element_by_xpath(datalistPath).click()
			i = 0
			while i < 20:
				try:
					i = i + 1
					m = str(i)
					# /html/body/div[2]/div/div[2]/div/ul/li[2]/a[2]
					path = "/html/body/div[2]/div/div[2]/div/ul/li[" + m + "]/a[2]"
					url = b.find_element_by_xpath(path).get_attribute("href")
					b.get(url)
					if b.find_element_by_id('att_btn').text == "已关注":
						print("已关注")
					else:
						b.find_element_by_id('att_btn').click()
					with open('myFan.txt', 'a') as fanData:
						fanData.write(url)
						fanData.write('\n')
					time.sleep(1)
				except:
					js = "var q=document.documentElement.scrollTop=10000"
					b.execute_script(js)
					time.sleep(1)
					continue
		except:
			js = "var q=document.documentElement.scrollTop=10000"
			b.execute_script(js)
			time.sleep(1)
		totalList=int(totalList)-1

#采集自己的关注数据
def attention_data():
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
	b.get("https://i.csdn.net/#/uc/follow-list")
	time.sleep(3)
	totalList=b.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]').text
	#b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]").click()
	totalList=int(totalList)
	myinterestList=[]
	while totalList >0 :
		try:
			totalList=str(totalList)
			datalistPath = '/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[' + totalList + ']'
			b.find_element_by_xpath(datalistPath).click()
			i = 0
			while i < 20:
				try:
					i = i + 1
					m = str(i)
					# /html/body/div[2]/div/div[2]/div/ul/li[2]/a[2]
					path = "/html/body/div[2]/div/div[2]/div/ul/li[" + m + "]/a[2]"
					uname = b.find_element_by_xpath(path).get_attribute()
					myinterestList.append(uname)
					# urlData = url.replace('article/details/', 'phoenix/article/digg?ArticleId=')
					with open('myInterest.txt', 'a') as fanData:
						fanData.write(uname)
						fanData.write('\n')
					time.sleep(1)
				except:
					js = "var q=document.documentElement.scrollTop=10000"
					b.execute_script(js)
					time.sleep(1)
					continue
		except:
			js = "var q=document.documentElement.scrollTop=10000"
			b.execute_script(js)
			time.sleep(1)
		totalList=int(totalList)-1
	return myinterestList

attention_data()




#attention_weixin()
#/html/body/div[2]/div/div[2]/div/ul/li[1]/a[3]
#/html/body/div[2]/div/div[2]/div/ul/li[20]/a[3]
#页数 8-3-4-4-4....
#/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[4]
#/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]
#/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]

# id已跑到794347

#b.find_element_by_xpath("/html/body/div[7]/ul/li[1]/button").click()
#/html/body/div[7]/ul/li[1]/button
#/html/body/div[7]/ul/li[1]/button