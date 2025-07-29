'''
    author: Adhyayan Wagle
    date: 28/07/25
    version: 1
    description: We will be making lists

'''

import random

name = input('Enetr your name:' )
age = int(input('Enter your age: '))

name = []

test = 5
for i in range(5):
    name.append(input("Enter a name: "))


for i in name:
    print(i)


