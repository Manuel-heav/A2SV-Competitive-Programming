class Solution(object):
    def countPairs(self, nums, target):
        counter = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i < j and (nums[i] + nums[j] < target)):
                    counter += 1
        return counter

        