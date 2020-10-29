class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        tmp = []
        ransomNoteArray = [xter for xter in ransomNote]
        magazineArray = [xter for xter in magazine]
        for x in range(len(ransomNoteArray)):
            for y in range(len(magazineArray)):
                if ransomNoteArray[x] == magazineArray[y]:
                    tmp.append(ransomNoteArray[x])
                    magazineArray.pop(y)  
                    break         
        if ''.join(tmp) == ransomNote:
            print("Works")
        else:
            print("Does not Work")


if __name__ == '__main__':
    #ransomNote = "aab" 
    #magazine = "baa"
    ransomNote = "aa"
    magazine = "ab"

    newSoln = Solution()
    newSoln.canConstruct(ransomNote, magazine)
