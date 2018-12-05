# __author:"wujianqinjian"
# __user:JianH
# __date:2018/12/4

from selenium import webdriver
import time

# attention_if_attention()该函数可完全自动重新关注自己的粉丝
def attention_if_attention():
    try:
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
        b.get("https://i.csdn.net/#/uc/fan-list")
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



def attention_myfan_data():
    try:
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
        b.get("https://i.csdn.net/#/uc/fan-list")
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


attention_if_attention()