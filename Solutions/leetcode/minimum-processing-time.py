class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        currMx = float("-inf")

        for i in range(len(tasks)):
            currMx = max(processorTime[i//4]+tasks[i], currMx)
        return currMx
