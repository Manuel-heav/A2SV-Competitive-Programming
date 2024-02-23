class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCount = nums.count(0)
        oneCount = nums.count(1)
        twoCount = nums.count(2)

        for i in range(zeroCount):
            nums.remove(0)
            nums.append(0)
        for i in range(oneCount):
            nums.remove(1)
            nums.append(1)
        for i in range(twoCount):
            nums.remove(2)
            nums.append(2)

        print(nums)


        