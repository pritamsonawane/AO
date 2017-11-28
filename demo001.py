# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:53:00 2017

@author: User
"""

class Employee:
    empCount=0
    raiseAmount = 1.4
    def __init__(self,name,salary):
        self.name= name
        self.salary = salary
        self.empCount +=1
        
    
    def __count(self):
        print "total employee=%d" %Employee.empCount
    
    
    def empDetail(self):
        print "name=%s ,salary= %d"% (self.name,self.salary)
    def raiseAmt(self):
        self.salary=int(self.salary * self.raiseAmount)
        return self.salary



emp1=Employee('pritam',25000)
emp2=Employee('rahul',232323)

emp2.empDetail()
print (emp1.raiseAmount)
print emp1.empCount


print emp1.__count()