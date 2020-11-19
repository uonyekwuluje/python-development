from typing import List
import time

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        print(nums)
        x = len(nums) - 1
        while x >= 0:
            if (nums[x] == val):
                del(nums[x])
                x = len(nums) - 1 
            else:
                x = x - 1
            time.sleep(1)
            print("Current Pass => {}".format(nums)) 
        return len(nums)  
            

if __name__ == '__main__':
    numArray = [0,1,2,2,3,0,4,2]
    num = 2
    newSoln = Solution()
    newSoln.removeElement(numArray,num)
