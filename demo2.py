# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:39:53 2017

@author: User
"""

string=raw_input("enter the string: ")
length=len(string)
for i in range(1,length):
    if i%2 == 0:
        print string[i],