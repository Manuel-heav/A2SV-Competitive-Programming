class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        numCount = Counter(arr)
        print(numCount)
        counts = list(numCount.values())
        counts.sort(reverse=True)
        
        for key in numCount:
            if numCount[key] == counts[0]:
                return key
