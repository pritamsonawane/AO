# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:02:37 2017

@author: User
"""
#print string in reverse order
string = raw_input("enter the string :")
length =len(string)
for i in range(length-1,0,-1):
    print string[i]