
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
			for line in open('testZan.txt', 'r'):
				line = line[:-1]
				str = line
				time.sleep(2)
				b.get(str)
				time.sleep(5)
		except:
			continue

attention_weixin()

# id已跑到794347
