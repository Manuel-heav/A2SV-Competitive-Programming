class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        toString = str(x)
        
        return toString == toString[::-1]