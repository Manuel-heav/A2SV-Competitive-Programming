class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        curr = s[:k]
        count = 0
        for i in range(len(curr)):
            if curr[i] in vowels:
                count += 1
        max_ = 0
        max_ = max(max_, count)
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                count -= 1

            if s[i] in vowels:
                count += 1
            max_ = max(max_, count)

        return max_
