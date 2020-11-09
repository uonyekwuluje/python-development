#!/usr/bin/env python3
from typing import List
from collections import Counter


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestString = ""
        shortestString = ""
        updateStr = ""

        if (len(strs) <=0 or len(strs) >=200):
            return ""  
         
        for x in range(len(strs)):
            if len(strs[x]) <= 0 or len(strs[x]) >= 200:
                return ""     
     

        # Find Longest String in Array
        for x in range(len(strs)): 
            if len(strs[x]) > len(longestString):
                longestString = strs[x]  
      
        # Find Shortest String in Array
        shortestString = longestString
        for x in range(len(strs)):
            if len(strs[x]) < len(shortestString):
                shortestString = strs[x]

       
        # Print Results
        print("The longest String => {}\nThe Shortest String => {}".format(longestString,shortestString))

        updateStr = ""
        currString = shortestString[0]
        isDiffFount = False       
       
        for x in range(len(shortestString)):
            currString = shortestString[0:x+1]
            for y in range(len(strs)):
                print("{} == {} => {}\n".format(currString,strs[y][0:x+1],(currString == strs[y][0:x+1])))
                if (currString != strs[y][0:x+1]):
                    isDiffFount = True
                    break  

            if(isDiffFount):
                break
            else:
                updateStr = currString
                isDiffFount = False  
          
        return updateStr
       

if __name__ == "__main__":
    strs = ["a"]
    #strs = ["flower","flow","flight"]
    #strs = ["flower","flow","flight","fiorena","floresence","fillabuster"]
    #strs = ["dog","racecar","car"]
    newSolution = Solution()
    #print("Least Common Prefix for {} => {}".format(strs,newSolution.longestCommonPrefix(strs))
    result = newSolution.longestCommonPrefix(strs)
    print("Least Common Prefix for {} => {}".format(strs,result))
