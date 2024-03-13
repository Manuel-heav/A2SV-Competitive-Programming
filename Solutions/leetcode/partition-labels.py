class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        N = len(s)

        for i in range(N):
            last[s[i]] = i

        counter, right = 0,0
        ans = []

        for i in range(N):
            counter += 1
            right = max(right, last[s[i]])

            if i == right:
                ans.append(counter)
                counter = 0
        return ans

            



































