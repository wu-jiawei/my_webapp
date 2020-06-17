'''
@Author: your name
@Date: 2020-06-17 10:04:00
@LastEditTime: 2020-06-17 10:11:20
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /my_webapp/superlists/lists/tests.py
'''
from django.test import TestCase

class SmokeTest(TestCase):
    
    def test_bad_math(self):
        self.assertEqual(1+1, 3)
