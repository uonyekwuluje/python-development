from typing import List

class Solution:
    """
    This code compute good pairs in a given array
    """
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for x in range(len(nums)):
            for y in range(x,len(nums)-1):
                if nums[x] == nums[y+1]:
                    #print("[{},{}]".format(nums[x],nums[y]))
                    count += 1
        return count 



if __name__ == '__main__':
    newsoln = Solution()
    testArrays = [[1,2,3,1,1,3],[1,1,1,1],[1,2,3]]
    for x in range(len(testArrays)):
         print("Array:=> {} | Number of good pairs:=> {}".format(testArrays[x], newsoln.numIdenticalPairs(testArrays[x])))
