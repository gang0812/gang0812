# a = [1,2,'6','summer']
# print('i' in a)
#
# dict_1 = {"class_id":45,'num':20}
# if dict_1['num'] > 5:
#       print(dict_1['num'])

# dic_1 = {"姓名：":"方方土","性别：":"男","年龄：":"20","城市：":"哈尔滨"}
# print(dic_1)
# dic_2 = {"姓名：":"齐木","性别：":"男","年龄：":"24","城市：":"莅临"}
# dic_3 = {"姓名：":"荷花","性别：":"女","年龄：":"23","城市：":"大连"}
# list1 = [dic_1,dic_2,dic_3]
# print(list1)
#
# count = 0
# list1 = ['房','七个','荷花','是有']
# for name in list1:
#     print(name)
#     count += 1
# print(count)
# print(len(list1))

# str1 = 'abcdefg'
# print(list(str1))
#
# int1 = range(10)
# print(int1)

# def add_fun(num):
#     sum = 0
#     for i in range(num):
#         sum +=i
#     print(sum)
# add_fun(100)
#
# def length1():
#     duixiang = input('请输入：')
#     if len(duixiang) > 5:
#         print(True)
#     else:
#         print(False)
#
# str1 = length1()


# def function_len(object):
#     if isinstance(object,dict) or isinstance(object,list) or isinstance(object,str):
#         leng = len(object)
#         if leng >5:
#             print('True')
#         else:
#             print('False')
#
#     else:
#         print('输入的数据有误')
# function_len('asdfgo')


# list1 = ['囧囧','唐生','旧模样']
# list2 = []
# list3 = ['male','female','female']
# list4 = ['12','15','34']
# list5 = ['哈尔滨','吉林','大连']
# for i in range(3):
#     dict1 = dict(name = list1[i],gander = list3[i],age = list4[i],city = list5[i])
#     list2.append(dict1)
# print(list2)
from selenium.webdriver.common.by import By
# import time
import time
# driver.implicitly_wait(5)
# driver.get("http://erp.lemfix.com/login.html")
# driver.maximize_window()
# driver.find_element(By.ID,'username').send_keys('test123')
# driver.find_element(By.ID,'password').send_keys('123456')
# time.sleep(2)
# # driver.find_element(By.ID,'btnSubmit').click()
# # driver.find_element(By.XPATH,"//button[@id='btnSubmit']").click()
# driver.find_element(By.XPATH,"//button[@id='btnSubmit']").click()
# login_user = driver.find_element(By.XPATH,"//p[text()='测试用户']").text
# if login_user == '测试用户':
#     print('这个登录的用户是：{}'.format(login_user))
# driver.find_element(By.XPATH,"//span[text()='零售出库']").click()
# id1 = driver.find_element(By.XPATH,"//div[text()='零售出库']//..").get_attribute("id")
# id2 = id1 +"-frame"
# driver.switch_to.frame(id2)
# driver.find_element(By.ID,'searchNumber').send_keys('247')
# driver.find_element(By.ID,"searchBtn").click()
def open_url(url,driver):
    driver.get(url)
def login(username,password,driver):
    driver.find_element(By.ID,'username').send_keys(username)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.ID, 'btnSubmit').click()
def search_key(driver,url,username,password,s_key):
    open_url(url,driver)
    login(username,password,driver)
    driver.find_element(By.XPATH, "//span[text()='零售出库']").click()
    ID1 = driver.find_element(By.XPATH, "//div[text() = '零售出库']//..").get_attribute('id')
    ID2 = ID1 + '-frame'
    driver.switch_to.frame(ID2)
    driver.find_element(By.ID, 'searchNumber').send_keys(s_key)
    driver.find_element(By.ID, 'searchBtn').click()
    time.sleep(1)
    num = driver.find_element(By.XPATH, "//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num