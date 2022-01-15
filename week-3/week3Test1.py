# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:06:56 2022

@author: ssssw
"""
#   import jason
import json
#   import urllib
import urllib.request as request
#   path
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
#   with open.url and save as raw, encoding
#   json 處理 json 資料格式
with request.urlopen(src) as response:
    raw=json.load(response)   
lens=len(raw["result"]["results"])
addsum=[]
for i in range(lens):  # O()=N
    site=raw["result"]["results"][i]["stitle"]
    area=raw["result"]["results"][i]["address"][5:8]
    ylong=raw["result"]["results"][i]["longitude"]
    xlati=raw["result"]["results"][i]["latitude"]
    picweb=raw["result"]["results"][i]["file"]
    picweb1=picweb.split('http',2) # 用split 把1st/2nd http分開 
    picweb2="http"+picweb1[1] # 還原1st網址到picweb2
    info=[site,area,ylong,xlati,picweb2]
    addsum.append(info)
#addsum 格式為[[a,b,c],[a,b,c],.......]
with open("data.csv", "w", encoding="utf-8") as file: #寫入data.csv
    x=len(addsum)
    for j in range(x):#O()=N
        file.write(addsum[j][0]+","+addsum[j][1]+","+addsum[j][2]+","
                   +addsum[j][3]+","+addsum[j][4]+",""\n")
          