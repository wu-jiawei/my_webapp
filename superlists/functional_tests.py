'''
@Author: your name
@Date: 2020-06-16 23:09:07
@LastEditTime: 2020-06-16 23:42:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /my_webapp/functionals_tests.py
'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title