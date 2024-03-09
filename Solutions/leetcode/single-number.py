class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        for key,value in numCount.items():
            if value == 1:
                return key
        