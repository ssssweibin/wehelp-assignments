# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 12:24:17 2022

@author: ssssw
"""

def maxProduct(nums):
    sum=nums[0]*nums[1]
    n=len(nums)
    for i in range(0,n):
        for j in range(1,n):
            if j<=i : continue
            elif sum>=nums[i]*nums[j]: continue
            else : sum=nums[i]*nums[j]
    print(sum)
maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])