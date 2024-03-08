class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")

        max_ = 0
        counter = 0

        for i in s[:-1]:
            if i == "1":
                ones -= 1
            if i == "0":
                counter += 1
            max_ = max(max_, ones+counter)
        return max_


        # s = list(map(int, s))
        # prefixSum = [0]*(len(s)+1)
        # for i in range(len(s)):
        #     prefixSum[i+1] = prefixSum[i] + s[i]
        
        # max_ = float("-inf")

        # for i in range(len(prefixSum)):
        #     max_ = max(max_, prefixSum[i] + len(prefixSum) - prefixSum[i])
        # return max_