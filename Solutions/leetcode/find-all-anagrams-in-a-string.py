class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        ans = []

        k = len(p)

        curr = Counter(s[:k])
        
        for i in range(k, len(s)):
            if counter == curr:
                ans.append(i-k) 
            if s[i] not in curr:
                curr[s[i]] = 1
            else:
                curr[s[i]] += 1
            if curr[s[i-k]] == 1:
                curr.pop(s[i-k])
            else:
                curr[s[i-k]] -= 1

        if curr == counter:
            ans.append(len(s)-len(p))
        
        return ans


        