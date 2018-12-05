
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
	b.get("https://BlogNet/passport_fe/login.html")
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
			#
			for newBlogNumber in range(1,100):
				newBlogNumber=str(newBlogNumber)
				b.get("https://blog.csdn.net/nav/newarticles")
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
		b.get("https://i.csdn.net/#/uc/follow-list")
		try:
			js = "var q=document.documentElement.scrollTop=100000"
			b.execute_script(js)
			time.sleep(1)
			b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]").click()
			time.sleep(1)
			# b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[4]").click()
			# time.sleep(1)
			for n in range(1,5):
				n = n + 1
				b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[3]").click()
				time.sleep(1)
				for m in range(1, 19):
					m = m + 1
					m = str(m)
					b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[" + m + "]/a[3]").click()
					time.sleep(0.2)
		except:
			continue
attention_weixin()
