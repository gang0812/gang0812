from test_code import test1
from test_data import test_data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
user = test_data.login_data[0]["username"]
pwd = test_data.login_data[1]["password"]
url = test_data.url['url']
s_key = test_data.s_key['s_key']
num = test1.search_key(driver=driver,url=url,username=user,password=pwd,s_key=s_key)
if s_key in num:
    print('测试通过')
else:
    print('测试未通过')