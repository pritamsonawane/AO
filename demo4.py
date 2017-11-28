# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:26:20 2017

@author: User
#"""
#Define a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print "Male" for Male class 
# and "Female" for Female class.

class Person:
    def getGender(self):
        print "this is person class"
        pass

class Male(Person):
    def getGender(self):
        print "This is a male class"

class Female(Person):
    def getGender(self):
        print "this is Female class"
    

m1=Male()
f1=Female()

m1.getGender()
f1.getGender()