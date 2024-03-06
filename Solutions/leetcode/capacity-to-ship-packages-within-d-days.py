class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def checker(num):
            sum_ = 0
            visit_counter = 1

            for i in range(len(weights)):
                if sum_ + weights[i] <= num:
                    sum_ += weights[i]
                else:
                    sum_ = weights[i]
                    visit_counter += 1 
            if visit_counter <= days:
                return True
            return False

        while left <= right:
            mid = (left + right)//2
            if checker(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
            

