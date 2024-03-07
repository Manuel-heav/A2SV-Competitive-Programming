class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        def check(num):
            thresh = []
            for i in range(len(nums)):
                thresh.append(ceil(nums[i]/num))
            if sum(thresh) <= threshold:
                return True
            return False
        
        while left <= right:
            mid = (right + left)//2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
        
        