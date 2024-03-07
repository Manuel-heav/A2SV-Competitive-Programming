class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        ans = 0
        while left <= right:
            mid = (left + right)//2
            point = len(citations) - mid
            if citations[mid] >= point:
                ans = point
                right = mid-1
            else:
                left = mid+1
        return ans



        