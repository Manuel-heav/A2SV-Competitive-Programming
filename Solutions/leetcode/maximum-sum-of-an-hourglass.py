class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
         ans = []
         for r in range(len(grid)-2):
             for c in range(len(grid[0])-2):
                ans.append(sum(grid[r][c:c+3]) + sum(grid[r+2][c:c+3]) + grid[r+1][c+1])
         return max(ans)      
                 