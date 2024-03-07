class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)-1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left = mid 
            else:
                right = mid 
        return nums[right]
        
        