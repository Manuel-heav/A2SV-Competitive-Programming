class Solution:
    def isPalindrome(self, x: int) -> bool:
        toString = str(x)
        
        return toString == toString[::-1]