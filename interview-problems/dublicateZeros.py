from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        print(arr)
        #inputS.append(1)
        #print(inputS)
        #inputS.pop()
        #print(inputS)
        #print(inputS[1:])
        #inputS.insert(4,9)
        #print(inputS)
        slen = len(arr)
        x = 0
        while x < slen:
            if arr[x] == 0:
               arr.insert(x+1,0)
               arr.pop()
               x += 2
            else:
               x += 1
        print(arr)


if __name__ == '__main__':
    inputS = [1,2,3]
    #inputS = [1,0,2,3,0,4,5,0]
    newSoln = Solution()
    newSoln.duplicateZeros(inputS)
