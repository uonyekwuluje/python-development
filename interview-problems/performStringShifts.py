from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
       sList = [xter for xter in s]
       for shiftx in shift:
           if shiftx[0] == 0:
               position = 0
               while position < shiftx[1]:
                   tempPop = sList.pop(0)
                   sList.append(tempPop)
                   position += 1
           elif shiftx[0] == 1:
               position = 0
               while position < shiftx[1]:
                   tempPop = sList.pop()
                   sList.insert(0,tempPop)
                   position += 1
       sString = ''.join(sList)
       return sString



if __name__ == '__main__':
    s = "abcdefg" 
    shift = [[1,1],[1,1],[0,2],[1,3]]
    newSoln = Solution()
    print("{} => {}".format(s,newSoln.stringShift(s,shift)))
