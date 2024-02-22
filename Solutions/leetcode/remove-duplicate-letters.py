class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        letterCounter = Counter(s)
        seen = set()

        for char in s:
            while stack and stack[-1] > char and char not in seen and letterCounter[stack[-1]] >= 1:
               seen.remove(stack.pop())            
            if char not in seen:
                stack.append(char)
            seen.add(char)
            letterCounter[char]-=1
        return "".join(stack)

            