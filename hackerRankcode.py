#!/bin/python

import sys
import re

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    matrix = []
    matrix_i = 0
    output=""
    for matrix_i in range(n):
        matrix_t = str(input())
        matrix.append(matrix_t)
    
    output=""
    for i in range(0,m):
        for x in matrix:
           output += x[i]
    nstr = re.sub(r'(?<=[A-Za-z])([^A-Za-z]+)(?=[A-Za-z])',' ',output)
    print (nstr)
    
   
           
      
    
 

            
   
    
    
            
