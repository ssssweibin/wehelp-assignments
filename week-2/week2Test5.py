# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:34:59 2022

@author: ssssw
"""
def maxZero(nums):
    n=len(nums)
    sum=0
    acc=0
    for i in range(0,n):
        if nums[i]!=0:
            acc=0
            continue
        elif acc<(sum): 
            acc=acc+1
            continue
        else: sum=sum+1;acc=acc+1
    print(sum)
maxZero([0,1,0,0,])
maxZero([1,0,0,0,0,1,0,1,0,0])
maxZero([1,1,1,1,1])
maxZero([0,0,0,1,1])
