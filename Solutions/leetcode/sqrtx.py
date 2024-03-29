class Solution:
    def mySqrt(self, x: int) -> int:
        low = -1
        high = x + 1
        ans = x
        while low + 1 < high:
            mid = (low + high)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid
            else:
                high = mid
        return low