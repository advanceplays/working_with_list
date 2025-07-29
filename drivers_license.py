'''
    author: Adhyayan Wagle
    date: 7/29/25
    version: 1
    description: This is a drivers license

'''

import random

name = input('Enter your name:')
age = int(input('Enter your age: '))

if age >= 16:
    print('You are eligible to have a restricted drivers license')
else:
    print('You are not eligible to have a restricted drivers license')