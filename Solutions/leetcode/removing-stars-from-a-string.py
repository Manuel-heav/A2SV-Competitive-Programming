class Solution:
    def removeStars(self, s: str) -> str:
        letterStack = []
        for i in range(len(s)):
            if s[i] != "*":
                letterStack.append(s[i])
            else:
                letterStack.pop()
        return "".join(letterStack)
        
        