class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [nums[0]]
        N = len(nums)

        for i in range(1, N):
            prefix.append(prefix[-1] + nums[i])
        
        counter = 0
        sums_ = Counter()

        for curr in prefix:
            if curr == k:
                counter += 1
            
            if curr - k in sums_:
                counter += sums_[curr - k]
            
            sums_[curr] += 1

        return counter