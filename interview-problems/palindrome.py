class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(x)
        xarray = [xt for xt in str(x)]
        revarray = xarray[::-1]
        newx = ''.join(revarray)
        if int(x) == int(newx) and isinstance(x, int):
            return True
        else:
            return False

if __name__ == '__main__':
    newSoln = Solution()
    num = 12341
    newSoln.isPalindrome(num)


s = str(x)
rs = "".join(list(reversed(s)))
if rs != s:
    return False
return True




"""
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        str_1 = str(abs(x))
        str_2 = str_1[::-1]
        if str_1 == str_2:
            return True
        else:
            return False
