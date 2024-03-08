class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        stack = []
        myDict = {}
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                stackTop = stack.pop()
                myDict[stackTop] = nums2[i]
            stack.append(nums2[i])
        
        for num in stack:
            myDict[num] = -1
        for num in nums1:
            answer.append(myDict[num])
        

        return answer
        