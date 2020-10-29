from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        numsLen = len(nums)
        newArray = []
        isFound = False

        if numsLen == 1 and nums[0] == target:
            newArray.append(0)
            newArray.append(0)
            return newArray

        for x in range(numsLen):
            if nums[x] == target:
                newArray.append(x)
                isFound = True
       
        if isFound:
            return newArray
        else:
            newArray.append(-1)
            newArray.append(-1)
            return newArray 


class Solution:
    def searchRange(self, nums, target):
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]



if __name__ == '__main__':
    #nums = [5,7,7,8,8,10]
    #target = 0
    nums = [1]
    target = 1
    newSoln = Solution()
    print(newSoln.searchRange(nums,target) )
