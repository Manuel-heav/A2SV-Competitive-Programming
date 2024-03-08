class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        elementArr = []
        max_ = float("-inf")
        for i in range(len(points)):
            elementArr.append(points[i][0])
        for i in range(len(points)-1):
            max_ = max(max_, elementArr[i] - elementArr[i-1])

        return max_
        