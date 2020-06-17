'''
@Author: your name
@Date: 2020-06-16 23:09:07
@LastEditTime: 2020-06-17 09:54:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /my_webapp/functionals_tests.py
'''
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('localhost:8000')
        
        # 网页的标题和头部应该包含'To-Do'这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        
if __name__ == "__main__":
    unittest.main()