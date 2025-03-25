class Solution(object):
    def isPalindrome(self, x):
        rev = 0

        if x >= 0:
            rev = int(str(x)[::-1])
            if rev == x:
                return True
            else:
                return False

        else:
            return False
        