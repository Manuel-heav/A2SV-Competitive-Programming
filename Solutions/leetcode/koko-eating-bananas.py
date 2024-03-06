class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checker(num):
            visited = 0
            for pile in piles:
                visited += ceil(pile/num)
            if visited <= h:
                return True
            return False

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right)//2
            if checker(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

        