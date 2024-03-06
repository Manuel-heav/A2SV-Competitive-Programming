class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        if target not in nums:
            return -1
        else:
            while low <= high:
                mid = (low + high)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
