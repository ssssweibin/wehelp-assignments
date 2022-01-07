# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 20:53:13 2022
Week-2 assignment1-python
@author: ssssw
"""
dataa={
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
     
}
def avg(data):
    cnt=data["count"]
    sum=0
    for n in range(cnt):
        ep=data["employees"][n]["salary"]
        sum=sum+ep
        n=n+1
    print(sum/data["count"])
avg(dataa)