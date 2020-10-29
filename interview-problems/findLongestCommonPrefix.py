from typing import List
from collections import Counter

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Test for empty array
        if not strs: 
           return ""

        for currString in range(len(strs)):
           if strs[currString] ==  "":
               return ""

        # Create dictionary and get the smallest element
        setDict = {} 
        for currString in range(len(strs)):
           setDict[strs[currString]] = len(strs[currString]) 
        c = Counter(setDict)
        smallestString = c.most_common()[len(strs)-1][0]
       
        if len(strs) == 1: 
            print (smallestString)
        
        # Test each subscript. update tmpstr if true and all counts equal on subscripts
        tmpStr = []
        isFound = False
        for x in range(len(smallestString)-1):
            for lstArray in range(len(strs)):
                if strs[lstArray][x] != smallestString[x]:
                    isFound = False
                    break
                else:
                    isFound = True
            if isFound:
                tmpStr.append(strs[lstArray][x]) 

            isFound = False
            count = 0

        # convert to string and print 
        print(''.join(tmpStr))


if __name__ == '__main__':
    newSoln = Solution()
    #inpArray = ["flower", "flow", "flight"]
    #inpArray = ["dog","racecar","car"] 
    #inpArray = ["a"]
    #inpArray = ["",""]
    #inpArray = ["a","b"]
    inpArray = ["c","c"]
    #inpArray = []
    newSoln.longestCommonPrefix(inpArray)
