
from selenium import webdriver
from string import Template
import time
import random
import requests

'''
人生总是时不时会有惊喜，之前的网站关注列表没有上一页和下一页的按钮，只能点击第4页，让列表页整体后移；比如：
1 2 3 4 5 ...55  点击“4”  2 3 4 5 6 ...55
这次直接点击“上一页”和“下一页”来控制，其实只有下一页，其实点到最后一页还有个异常没有处理，先上传吧，后续有空再改
'''

# 修复自动关注自己的粉丝bug
# 智能再次关注自己的粉丝
def attention_myfan():
    i = 84720
    b = webdriver.Chrome()
    b.maximize_window()
    b.get("https://passport.博客地址.net/passport_fe/login.html")
    b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
    b.find_element_by_id("all").send_keys("自己的用户名")
    time.sleep(3)
    b.find_element_by_id("password-number").send_keys("自己的密码")
    time.sleep(3)
    b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button").click()
    time.sleep(3)
    b.get("https://博客地址/#/uc/fan-list")
    time.sleep(2)
    while i > 1:
        i = i - 1
        js = "var q=document.documentElement.scrollTop=100000"
        b.execute_script(js)
        time.sleep(1)
        isSix = 6
        # /html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[6]
        # /html/body/div[2]/div/div[2]/div/div[2]/div/button[2]  下一页
        # /html/body/div[2]/div/div[2]/div/div[2]/div/button[2]
        # b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li["+isSix+"]").click()
        # time.sleep(1)
        #查看总共多少页
        total = b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]").text
        total=int(total)
        print(type(total))
        print(total)
        for n in range(1, total):
            n = n + 1
            # /html/body/div[2]/div/div[2]/div/ul/li[20]/a[3]
            # /html/body/div[2]/div/div[2]/div/ul/li[1]/a[3]
            #点击下一页
            b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/button[2]").click()
            time.sleep(1)
            for m in range(0, 19):
                m = m + 1
                m = str(m)
                time.sleep(0.3)
                userStatu=b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[" + m + "]/a[3]").text
                if userStatu == "关注":
                    time.sleep(0.3)
                    b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[" + m + "]/a[3]").click()
                    time.sleep(0.3)
                    print("关注成功")
                else:
                    print("已关注")

#取消自己已经关注的用户
def attentioned_cancle():
    i = 84720
    b = webdriver.Chrome()
    b.maximize_window()
    b.get("https://passport.博客地址.net/passport_fe/login.html")
    b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
    b.find_element_by_id("all").send_keys("自己的用户名")
    time.sleep(3)
    b.find_element_by_id("password-number").send_keys("自己的密码")
    time.sleep(3)
    b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button").click()
    time.sleep(3)
    b.get("https://博客地址/#/uc/follow-list")
    time.sleep(2)
    while i > 1:
        i = i - 1
        js = "var q=document.documentElement.scrollTop=100000"
        b.execute_script(js)
        time.sleep(1)
        isSix = 6
        # /html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[6]
        # /html/body/div[2]/div/div[2]/div/div[2]/div/button[2]  下一页
        # /html/body/div[2]/div/div[2]/div/div[2]/div/button[2]
        # b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li["+isSix+"]").click()
        # time.sleep(1)
        #查看总共多少页
        total = b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]").text
        total=int(total)
        print(type(total))
        print(total)
        for n in range(1, total):
            n = n + 1
            # /html/body/div[2]/div/div[2]/div/ul/li[20]/a[3]
            # /html/body/div[2]/div/div[2]/div/ul/li[1]/a[3]
            #点击下一页
            b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/button[2]").click()
            time.sleep(1)
            for m in range(0, 19):
                m = m + 1
                m = str(m)
                userStatu=b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[" + m + "]/a[3]").text
                if userStatu == "取消关注":
                    time.sleep(0.3)
                    b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[" + m + "]/a[3]").click()
                    time.sleep(0.3)
                    print("取消成功")
                else:
                    print("已取消关注")


#取消关注自己的粉丝用户
def faned_cancle():
    i = 84720
    b = webdriver.Chrome()
    b.maximize_window()
    b.get("https://passport.博客地址.net/passport_fe/login.html")
    b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
    b.find_element_by_id("all").send_keys("自己的用户名")
    time.sleep(3)
    b.find_element_by_id("password-number").send_keys("自己的密码")
    time.sleep(3)
    b.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button").click()
    time.sleep(3)
    b.get("https://博客地址/#/uc/fan-list")
    time.sleep(2)
    while i > 1:
        i = i - 1
        js = "var q=document.documentElement.scrollTop=100000"
        b.execute_script(js)
        time.sleep(1)
        isSix = 6
        # /html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[6]
        # /html/body/div[2]/div/div[2]/div/div[2]/div/button[2]  下一页
        # /html/body/div[2]/div/div[2]/div/div[2]/div/button[2]
        # b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li["+isSix+"]").click()
        # time.sleep(1)
        #查看总共多少页
        total = b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/ul/li[8]").text
        total=int(total)
        print(type(total))
        print(total)
        for n in range(1, total):
            n = n + 1
            # /html/body/div[2]/div/div[2]/div/ul/li[20]/a[3]
            # /html/body/div[2]/div/div[2]/div/ul/li[1]/a[3]
            #点击下一页
            b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/button[2]").click()
            time.sleep(1)
            for m in range(0, 19):
                m = m + 1
                m = str(m)
                userStatu=b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[" + m + "]/a[3]").text
                if userStatu == "取消关注":
                    time.sleep(0.3)
                    b.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[" + m + "]/a[3]").click()
                    time.sleep(0.3)
                    print("取消成功")
                else:
                    print("已取消关注")




attention_myfan()