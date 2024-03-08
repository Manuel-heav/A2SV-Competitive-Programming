class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        curr = sum(nums[:k])
        max_ = curr/k

        for r in range(k, len(nums)):
            curr += nums[r] - nums[r-k]
            max_ = max(max_, curr/k)
        return max_
            
                



        