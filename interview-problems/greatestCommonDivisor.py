class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        demLen = len(str2)
        strChunks = [str1[i:i+demLen] for i in range(0, len(str1), demLen)]
        isContains = False
        for x in range(len(strChunks)):
            if strChunks[x] == str2:
                isContains = True
            else:
                isContains = False  
            #print(strChunks[x], isContains)
        if (strChunks[len(strChunks)-1] in str2):
            return (strChunks[len(strChunks)-1])
        else:
            return '""'  

        #if not strChunks[0] == str2:
        #    return ""
        #else:
        #    return (strChunks[len(strChunks)-1])
      

if __name__ == '__main__':
    newSoln = Solution()
    str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    print(newSoln.gcdOfStrings(str1,str2))
