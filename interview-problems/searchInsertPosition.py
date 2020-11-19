from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       if (len(nums) == 1):
          if (target < nums[0]):
              return 0
          else:
              return 1

       elif (target in nums):
           for x in range(len(nums)):
               if nums[x] == target:
                   return x
       else:
           strLen = len(nums)
           x = 1
           while x < strLen:
                if (target < nums[x-1] and target < nums[x]):
                   return (x-1)
                elif (target > nums[x-1] and target < nums[x]):
                   return (x)
                elif (target > nums[len(nums)-1]):
                   return (len(nums))
                elif (target > nums[x-1] and target > nums[x]):
                   return (x+1)
                else: 
                   x += 1

if __name__ == '__main__':
    numArray = [1]
    #numArray = [1,3,5,6]
    num = 0
    newSoln = Solution()
    print(numArray)
    print(newSoln.searchInsert(numArray,num))
