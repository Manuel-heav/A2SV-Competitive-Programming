class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        count = []
        for i in range(rows - 1):
            for j in range(cols):
                if strs[i][j] > strs[i+1][j]:
                    count.append(j)
                    
        return len(set(count))