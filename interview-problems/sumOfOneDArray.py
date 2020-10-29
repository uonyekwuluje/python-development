from typing import List

class Solution:
    """
    This code computes the sum of 1 dimensional array
    """
    def runningSum(self, nums: List[int]) -> List[int]:
        newArray = []
        for x in range(len(nums)):
            sumn = 0  
            for y in range(x+1):
                sumn += nums[y]
            newArray.append(sumn) 
        return(newArray)

if __name__ == '__main__':
    newsoln = Solution()
    testArrays = [[1,2,3,4],[1,1,1,1,1],[3,1,2,10,1]]
    for x in range(len(testArrays)):
         print("Array:=> {}   | Sum of Array:=> {}".format(testArrays[x], newsoln.runningSum(testArrays[x])))
