class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCount = nums.count(0)
        for i in range(zeroCount):
            nums.remove(0)
        for i in range(zeroCount):
            nums.append(0)
        
        