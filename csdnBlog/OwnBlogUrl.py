
from selenium import webdriver
from string import Template
import time
import random

#微信版
def attention_weixin():
	i=1
	b = webdriver.Chrome()
	b.maximize_window()
	b.get("https://blog.csdn.net/u010569419/article/list/1?t=1")
	#b.find_element_by_xpath("/html/body/div[2]/div/main/ul/li[1]/div/div[1]/h2/a").click()
	while i < 20:
		try:
			i = i + 1
			m = str(i)
			url = "/html/body/div[3]/main/div[2]/div[" + m + "]/h4/a"
			c = b.find_element_by_xpath(url).get_attribute("href")
			# time.sleep(1)
			#time.sleep(1)
			print(c)
		except:
			js = "var q=document.documentElement.scrollTop=100000"
			b.execute_script(js)
			time.sleep(3)
			continue

	#f.close()
attention_weixin()

# id已跑到794347