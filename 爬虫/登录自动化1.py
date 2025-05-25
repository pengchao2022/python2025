from selenium import webdriver #webdriver 具有浏览器的功能
import time
from constants import LOGIN_NAME, LOGIN_PASS

#创建一个浏览器对象
driver = webdriver.Chrome()

#根据浏览器对象执行浏览器的自动化操作
driver.get('https://www.lagou.com/')
driver.implicitly_wait(10) #隐式等待，浏览器加载页面需要时间，智能化的等待
driver.maximize_window() #最大化浏览器窗口

time.sleep(1)
#自动点击登录
SELECTOR_LOGIN = '#lg_tbar > div.lg_tbar_r > ul > li:nth-child(1) > a'
login_label = driver.find_element("css selector", SELECTOR_LOGIN)
login_label.click()

time.sleep(3)

#点击密码登录
SELECTOR_PASSLOGIN = 'body > div:nth-child(40) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div.sc-cTAqQK.hvfJvE > div.sc-iAKWXU.cvvlHK > div.sc-ksdxgE.xiHng > div > div.sc-fotOHu.fLmipN > div.sc-giYglK.gKjFct > div'
pass_login = driver.find_element("css selector", SELECTOR_PASSLOGIN)
pass_login.click()
time.sleep(2)


#输入用户名
SELECTOR_USERNAME = 'body > div:nth-child(40) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div.sc-cTAqQK.hvfJvE > div.sc-iAKWXU.cvvlHK > div.sc-ksdxgE.xiHng > div > div.sc-fotOHu.fLmipN > div:nth-child(1) > input'
user_name = driver.find_element("css selector", SELECTOR_USERNAME)
user_name.send_keys(LOGIN_NAME)
time.sleep(2)

#输入密码
SELECTOR_PASSWORD = 'body > div:nth-child(40) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div.sc-cTAqQK.hvfJvE > div.sc-iAKWXU.cvvlHK > div.sc-ksdxgE.xiHng > div > div.sc-fotOHu.fLmipN > div:nth-child(2) > input'
pass_word = driver.find_element("css selector", SELECTOR_PASSWORD)
pass_word.send_keys(LOGIN_PASS)
time.sleep(2)

#点击“登录”
SELECTOR_CLICK_LOGIN = 'body > div:nth-child(40) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div.sc-cTAqQK.hvfJvE > div.sc-iAKWXU.cvvlHK > div.sc-fFeiMQ.VKAnA > button > span'
click_login = driver.find_element("css selector", SELECTOR_CLICK_LOGIN)
click_login.click()



time.sleep(30)
#关闭网站
driver.quit()
#当打开浏览器对象以后，后续的一切操作（代码编写）和平常浏览器的操作大致一样
