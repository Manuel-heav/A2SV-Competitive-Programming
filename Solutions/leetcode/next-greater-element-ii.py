class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        arr = [-1] * n
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                num = stack.pop()
                arr[num] = nums[i % n]
            stack.append(i % n)
        return arr