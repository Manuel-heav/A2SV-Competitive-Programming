class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        bucket = []
        N = len(candidates)
        candidates.sort()
        def backtrack(i):
            if sum(bucket) == target:
                ans.append(bucket[:])
                return

            if i < len(candidates):
                if sum(bucket) < target:
                    bucket.append(candidates[i])
                    backtrack(i)
                    bucket.pop()
                    backtrack(i+1)
        backtrack(0)
        return ans