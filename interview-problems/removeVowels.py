class Solution:
    def removeVowels(self, S: str) -> str:
       strgVowels="aeiou"
       narray = []
       for x in S:
           if x not in strgVowels:
              narray.append(x)
       newString = ''.join(map(str,narray))
       return newString     

if __name__ == '__main__':
    newsoln = Solution()
    strg="leetcodeisacommunityforcoders"
    newsoln.removeVowels(strg)
