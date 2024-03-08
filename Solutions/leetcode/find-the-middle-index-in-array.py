class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixSum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefixSum[i+1] = prefixSum[i] + nums[i]

        for i in range(1, len(prefixSum)):
            if prefixSum[i-1] ==  prefixSum[-1] - prefixSum[i]:
                return i-1
        return -1

