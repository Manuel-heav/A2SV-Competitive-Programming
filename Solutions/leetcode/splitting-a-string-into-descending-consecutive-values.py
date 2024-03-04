class Solution:
    def splitString(self, s: str) -> bool:
        numbers = []

        def backtrack(curr):
            if curr >= len(s):
                for i in range(1, len(numbers)):
                    if numbers[i-1] - numbers[i] != 1:
                        return False
                return len(numbers) >= 2

            for i in range(curr, len(s)):
                val = int(s[curr:i+1])
                if len(numbers) == 0 or val == numbers[-1] - 1:
                    numbers.append(val)
                    if backtrack(i+1):
                        return True 
                    numbers.pop() 

            return False
        return backtrack(0)
        