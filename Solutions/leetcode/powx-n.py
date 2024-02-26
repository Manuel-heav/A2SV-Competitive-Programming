class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == 2:
            return x * x
        if n < 0:
            return 1 / (self.myPow(x, abs(n)))

        if n % 2 == 0:
            return self.myPow(x*x, n // 2) 
        else:
            return self.myPow(x, n-1) * x

            
        