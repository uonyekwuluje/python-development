from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                index_sum = nums[x] + nums[y]
                if index_sum == target:
                    return ([x,y]) 
  
            

if __name__ == '__main__':
    numArray = [2,6,8,1]
    num2 = 9
    newSoln = Solution()
    print(newSoln.twoSum(numArray,num2))
