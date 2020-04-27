#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 12:02
# @Author  : TanLHHH
# @Site    : 
# @File    : Webdriver_test.py
# @Software: PyCharm
#!/usr/bin/python
#coding:utf-8

from selenium import webdriver
import time
username = '15736096955'
password = 'tlh078797'
driver = webdriver.Chrome()
driver.get("https://www.renrendai.com/login")
driver.find_element_by_class_name("tab-password").click()  # 点击密码登录(在隐藏模块)
time.sleep(2)
driver.find_element_by_id("login_username").send_keys(username)
time.sleep(2)  # 设置等待时间，不用修改
driver.find_element_by_id("J_pass_input").send_keys(password)
time.sleep(5)  # 设置等待时间，以防止用户名下拉菜单挡住登录按钮
driver.find_element_by_id("rememberme-login").click()
time.sleep(2)
driver.find_element_by_class_name("button-block").click()  # 点击登录

