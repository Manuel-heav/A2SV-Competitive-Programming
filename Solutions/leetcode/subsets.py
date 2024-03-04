class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        bucket = []

        def backtrack(i):
            if i >= N:
                ans.append(bucket[:])
                return 
            bucket.append(nums[i])
            backtrack(i+1)
            bucket.pop()
            backtrack(i+1)        
        backtrack(0)
        return ans






        