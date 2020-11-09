#!/usr/bin/env python3
from typing import List
from collections import Counter


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = list(dict.fromkeys(nums))

        return nums
        #return len(retVal), "nums = retVal  

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newDict = {}
        for x in range(len(nums)):
            if nums[x] not in newDict:
                newDict[nums[x]] = 1
            else:
                newDict[nums[x]] = 1

        retVal = []
        for x,y in newDict.items():
            retVal.append(x)

        return retVal
        #return len(retVal), "nums = retVal  


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                del nums[i]
        return len(nums)
'''


if __name__ == "__main__":
    #nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1,1,2]
    newSolution = Solution()
    print(newSolution.removeDuplicates(nums))
    #print("List => {} | Return => {}\n".format(nums,newSolution.removeDuplicates(nums)))

