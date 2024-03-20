class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        sum_ = 0

        min_ = float("inf")

        for r in range(len(nums)):
            sum_ += nums[r]
            print(sum_)
            while sum_ >= target:
                min_ = min(min_, r-left + 1)
                sum_ -= nums[left]
                left += 1
        return 0 if min_ == float("inf") else min_  

            
        