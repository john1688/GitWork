
from selenium import webdriver
from string import Template
import time
import random

#微信版
def attention_weixin():
	i=880000
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
		try:
			i = i - 1
			print("i的值：  ", i)
			m=""
			m= str(i)
			url = "https://me.csdn.net/weixin_43" + m
			print("---------")
			b.get(url)
			time.sleep(1)
			mn=b.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/div/ul/li[3]/span").text
			mn2=b.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/div/ul/li[6]/span").text
			mn=int(mn)
			mn2 = int(mn2)
			print(mn)
			if mn > 5 & mn2 > 0:
				print(type(mn))
				b.find_element_by_id("att_btn").click()
				# time.sleep(1)
				print(url)
				print("---------")
				# i = int(i)
				print(i)
			else:
				print("true")
		except:
			continue

attention_weixin()

# id已跑到794347