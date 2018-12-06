
from selenium import webdriver
import time
import random

def rblog():
	for line in open('c:/test.txt','r'):
		line = line[:-1]
		str = line
		option=webdriver.ChromeOptions()
		option.add_argument('headless')
		#b = webdriver.Chrome('C:\Program Files (x86)\Google\chromedriver.exe')
		b = webdriver.Chrome(chrome_options=option)
		b.get(str)
		b.close()
		ran = random.randint(3, 15)
		time.sleep(ran)

def test():
	while 1<2:
		rblog()


test()

