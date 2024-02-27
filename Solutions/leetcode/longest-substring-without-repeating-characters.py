class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new = []
        final = []
        for i in range(len(s)):
            temp = ""
            for j in range(i, len(s)):
                if s[j] not in temp:
                    temp += s[j]
                else: 
                    break
                new.append(temp)
        if not new:
            return 0
        longest = max(new, key=lambda x: len(x))
        return len(longest)
        
