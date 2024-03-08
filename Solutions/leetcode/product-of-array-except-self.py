class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = [1]*(len(nums)+1)
        suffixProd = [1]*(len(nums)+1)

        for i in range(len(nums)):
            prefixProd[i+1] = prefixProd[i]*nums[i]


        for i in range(len(nums)-1, -1,-1):
            suffixProd[i] = suffixProd[i+1]*nums[i]
        
        answer = []
        for i in range(len(nums)):
            answer.append(prefixProd[i] * suffixProd[i+1])
        return answer        