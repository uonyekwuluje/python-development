class Solution:
    def firstUniqChar(self, s: str) -> int:
        xterFound = ""

        strDict = {}
        for x in range(len(s)):
            if s[x] in strDict:
                strDict[s[x]] += 1
            else:
                strDict[s[x]] = 1

        for key,value in strDict.items():
            if value == 1:
                #print("Unique Value | {},{}".format(key,value))
                xterFound = key
                break

        for x in range(len(s)):
            if s[x] == xterFound:
                return x


class Solution2:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1



if __name__ == '__main__':
    #testString = "leetcode"
    testString = "loveleetcode"
    testSoln = Solution()
    print(testSoln.firstUniqChar(testString))
