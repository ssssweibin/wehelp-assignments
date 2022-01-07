# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:34:59 2022

@author: ssssw
"""
def twoSum(nums,target):
    n=len(nums)
    for i in range(0,n):
        for j in range(1,n):
            if j<=i : continue
            elif nums[i]+nums[j]==target : return [i,j]
            else: continue  
result=twoSum([2,11,8,15],9)
print(result)