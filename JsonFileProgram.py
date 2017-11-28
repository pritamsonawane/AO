# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:10:26 2017

@author: User
"""
import json

from dateutil import parser
from datetime import datetime

    

with open("input.json") as json_file:
    json_data = json.load(json_file)


d1 = json_data['DOB']
d11 = parser.parse(d1)
d2 =datetime.today()
dayss = (d2 - d11).days


data={
      "STATUS_CODE": 200,
      "MESSAGE" : "Welcome "+json_data['NAME'],
      "RESULT" : {"DAYS" : dayss,
                  "ADDRESS" : json_data['ADDRESS']}
    }

print data

with open("output2.json",'w+') as op:
    json.dump(data,op)
    



    

    
    





