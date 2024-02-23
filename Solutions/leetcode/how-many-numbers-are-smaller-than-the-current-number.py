class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            countNum = sum(1 for element in nums if element < nums[i])
            final.append(countNum)
        return final

