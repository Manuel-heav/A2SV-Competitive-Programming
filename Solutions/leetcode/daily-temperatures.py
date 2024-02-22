class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexCount = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                l = stack.pop()
                indexCount[l] = i - l
            stack.append(i)
        return indexCount
            
