class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsArr = set(nums)
        missing = -1
        for i in range(len(nums)+1):
            if i not in numsArr:
                missing = i
        return missing