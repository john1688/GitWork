
from selenium import webdriver
import time
import random

def rblog(ran):
	i=random.randint(1,5)
	if i == 1:
		for line in open('c:/test.txt', 'r'):
			line = line[:-1]
			str = line
			#b = webdriver.Chrome('C:\Program Files (x86)\Google\chromedriver.exe')
			option=webdriver.ChromeOptions()
			option.add_argument('headless')
			option.add_argument('--disable-gpu')
			#b = webdriver.Chrome('C:\Program Files (x86)\Google\chromedriver.exe')
			b = webdriver.Chrome(chrome_options=option)
			b.get(str)
			b.close()
			b.quit()
			time.sleep(2)
	elif i == 2:
		for line in open('c:/test1.txt', 'r'):
			line = line[:-1]
			str = line
			option = webdriver.ChromeOptions()
			option.add_argument('headless')
			option.add_argument('--disable-gpu')
		  	#b = webdriver.Chrome('C:\Program Files (x86)\Google\chromedriver.exe')
			b = webdriver.Chrome(chrome_options=option)
			b = webdriver.Chrome('C:\Program Files (x86)\Google\chromedriver.exe')
			b.get(str)
			b.close()
			b.quit()
			time.sleep(ran+1)
	elif i == 3:
		for line in open('c:/test2.txt', 'r'):
			line = line[:-1]
			str = line
			option=webdriver.ChromeOptions()
			option.add_argument('headless')
			option.add_argument('--disable-gpu')
			#b = webdriver.Chrome('C:\Program Files (x86)\Google\chromedriver.exe')
			b = webdriver.Chrome(chrome_options=option)
			b.get(str)
			b.close()
			b.quit()
			time.sleep(ran*ran)
	elif i == 4:
		for line in open('c:/test3.txt', 'r'):
			line = line[:-1]
			str = line
			option=webdriver.ChromeOptions()
			option.add_argument('headless')
			option.add_argument('--disable-gpu')
			#b = webdriver.Chrome('C:\Program Files (x86)\Google\chromedriver.exe')
			b = webdriver.Chrome(chrome_options=option)
			b.get(str)
			b.close()
			b.quit()
			time.sleep(ran*ran)
	else :
		for line in open('c:/test4.txt', 'r'):
			line = line[:-1]
			str = line
			option=webdriver.ChromeOptions()
			option.add_argument('headless')
			option.add_argument('--disable-gpu')
			#b = webdriver.Chrome('C:\Program Files (x86)\Google\chromedriver.exe')
			b = webdriver.Chrome(chrome_options=option)
			b.get(str)
			b.close()
			b.quit()
			time.sleep(ran*ran)


def test():
	while 1<2:
		ran=random.randint(1,4)
		rblog(ran)


test()