#!/usr/bin/env python3
from typing import List
from collections import Counter


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:    
            nlist = s.split()  
            return ''.join(nlist[-1:])

if __name__ == "__main__":
    strs = ""
    #strs = "Hello World. Saying some good things buddy"
    newSolution = Solution()
    print(newSolution.lengthOfLastWord(strs))
