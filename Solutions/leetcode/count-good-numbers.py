class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9) + 7
        def power(x, n):
            mod = (10**9) + 7
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n == 2:
                return x * x
            if n < 0:
                return 1 / (self.myPow(x % mod, abs(n)))
            if n % 2 == 0:
                return power(x*x % mod, n // 2) 
            else:
                return power(x % mod, n-1) * x
        fourCount = floor(n / 2)
        fiveCount = ceil(n / 2)
        
        return power(4, fourCount) * power(5, fiveCount) % mod