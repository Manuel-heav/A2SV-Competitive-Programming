class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        finalArr = []
        counter = 0
        for i in range(len(nums)):
            counter+=nums[i]
            finalArr.append(counter)
        return finalArr
