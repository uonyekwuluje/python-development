class Solution:
    def reverse(self, x: int) -> int:
        nstring = [xt for xt in str(x)]
        
        if nstring[0] == '-' and len(nstring) > 1:
           nstring.pop(0)
           revstring = nstring[::-1]      
           stripzero = ''.join(revstring).lstrip("0")
           stripzero1 = [xter for xter in stripzero]
           stripzero1.insert(0,'-')
           if int(''.join(stripzero1)) >= -2147483648 and int(''.join(stripzero1)) <= 2147483647:
               return ''.join(stripzero1)
           else:
               return 0    
        elif nstring[0] == '0' and len(nstring) == 1:
           return 0
        else:
           revstring = nstring[::-1]
           stripzero = ''.join(revstring).lstrip("0")
           stripzero1 = [xter for xter in stripzero]
           if int(''.join(stripzero1)) >= -2147483648 and int(''.join(stripzero1)) <= 2147483647:
               return ''.join(stripzero1)
           else:
               return 0
 
 

if __name__ == '__main__':
    num = 123
    newSoln = Solution()
    print("Number => {}\nReverse => {}\n".format(num,newSoln.reverse(num)))
