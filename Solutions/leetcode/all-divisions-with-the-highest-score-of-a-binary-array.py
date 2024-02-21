class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        oneCount = nums.count(1)
        current_zero = 0
        itemDict = {}
        itemDict[0] = current_zero + oneCount

        for i in range(len(nums)+1):
            itemDict[i] = oneCount + current_zero
            if i<len(nums) and nums[i] == 1:
                oneCount -= 1
            if i<len(nums) and  nums[i] == 0:
                current_zero += 1
    
        current_max = 1
        final = []
        indexArr = list(itemDict.values())
        for i in range(len(indexArr)):
            if indexArr[i] == current_max:
                final.append(i)
            elif indexArr[i] > current_max:
                final = [i]
                current_max = indexArr[i]
        
        return final      
        


        