
from selenium import webdriver
from string import Template
import time
import random
import requests

#判断是否为已关注，否则点击关注
def attention_if():
	i=84720
	b = webdriver.Chrome()
	b.maximize_window()
	b.get("https://****.net/login#/uc/profile")
	b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
	b.find_element_by_id("all").send_keys("testName")
	time.sleep(3)
	b.find_element_by_id("password-number").send_keys("testPassword")
	time.sleep(3)
	b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button").click()
	time.sleep(3)
	while i > 1:
		i = i - 1
		try:
			#
			for newBlogNumber in range(20,100):
				newBlogNumber=str(newBlogNumber)
				b.get("https://blog.blog*******.net/nav/newarticles")
				time.sleep(0.8)
				newBlogPath = "/html/body/div[2]/div/main/ul/li[" + newBlogNumber + "]/div/div[1]/h2/a"
				newBlogUrl = b.find_element_by_xpath(newBlogPath).get_attribute("href")
				b.get(newBlogUrl)
				time.sleep(0.5)
				attentionStatus = b.find_element_by_xpath('//*[@id="btnAttent"]').text
				if attentionStatus == '已关注':
					newBlogUrl=str(newBlogUrl)
					attentionNewBlogUrl=newBlogUrl.replace("article/details/","phoenix/article/digg?ArticleId=")
					b.get(attentionNewBlogUrl)
					time.sleep(1)
					print("已关注: ")
				else:
					b.find_element_by_xpath('//*[@id="btnAttent"]').click()
					newBlogUrl = str(newBlogUrl)
					attentionNewBlogUrl = newBlogUrl.replace("article/details/", "phoenix/article/digg?ArticleId=")
					b.get(attentionNewBlogUrl)
					time.sleep(0.5)
		except:
			js = "var q=document.documentElement.scrollTop=100000"
			b.execute_script(js)
			time.sleep(3)
			continue

#自动重新关注自己的粉丝
def attention_myFan():
    try:
        b = webdriver.Chrome()
        b.maximize_window()
        b.get("https://****.net/login#/uc/profile")
        b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
        b.find_element_by_id("all").send_keys("")
        time.sleep(3)
        b.find_element_by_id("password-number").send_keys("")
        time.sleep(3)
        b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button").click()
        time.sleep(3)
        b.get("https://i.blog*******.net/#/uc/fan-list")
        time.sleep(2)
        js = "var q=document.documentElement.scrollTop=100000"
        b.execute_script(js)
        time.sleep(3)
        b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]").click()
        time.sleep(1)
        for l in range(1,15):
            try:
                l=str(l)
                b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li["+l+"]").click()
                for i in range(1, 20):
                    try:
                        i = str(i)
                        statuAttention = b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[" + i + "]/a[3]").get_attribute("text")
                        if statuAttention == "关注":
                            b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[" + i + "]/a[3]").click()
                            time.sleep(1)
                        else:
                            print(statuAttention)
                    except:
                        continue
            except:
                continue
    except:
        print("test")
#将关注列表的用户放弃关注
def attention_weixin():
	i=84720
	b = webdriver.Chrome()
	b.maximize_window()
	b.get("https://****.net/login#/uc/profile")
	b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
	b.find_element_by_id("all").send_keys("")
	time.sleep(3)
	b.find_element_by_id("password-number").send_keys("")
	time.sleep(3)
	b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button").click()
	time.sleep(3)
	b.get("https://i.blog*******.net/#/uc/follow-list")
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
#简单的点赞功能
def attention_admire():
	i=84720
	b = webdriver.Chrome()
	b.maximize_window()
	b.get("https://****.net/login#/uc/profile")
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
			for line in open('testZan.txt', 'r'):
				line = line[:-1]
				str = line
				time.sleep(2)
				b.get(str)
				time.sleep(5)
		except:
			continue


#采集自己的粉丝数据
def attention_fan():
	b = webdriver.Chrome()
	b.maximize_window()
	b.get("https://****.net/login#/uc/profile")
	b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
	b.find_element_by_id("all").send_keys("")
	time.sleep(3)
	b.find_element_by_id("password-number").send_keys("")
	time.sleep(3)
	b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button").click()
	time.sleep(3)
	b.get("https://i.blog*******.net/#/uc/fan-list")
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
	b.get("https://****.net/login#/uc/profile")
	b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
	b.find_element_by_id("all").send_keys("")
	time.sleep(3)
	b.find_element_by_id("password-number").send_keys("")
	time.sleep(3)
	b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button").click()
	time.sleep(3)
	b.get("https://i.blog*******.net/#/uc/follow-list")
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











