class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, len(nums)
        ans = []
        isFound = False
        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] == target:
                isFound = True
            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        if not isFound:
            ans.append(-1)
        else:
            ans.append(right)

        left = right - 1
        right = len(nums)
    
        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        if not isFound:
            ans.append(-1)
        else:
            ans.append(left)

        return ans