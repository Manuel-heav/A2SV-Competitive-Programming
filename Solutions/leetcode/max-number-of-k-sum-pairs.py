class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        counter = 0
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] == k:
                print(nums[left], nums[right])
                left += 1
                right -= 1
                counter += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        return counter
        