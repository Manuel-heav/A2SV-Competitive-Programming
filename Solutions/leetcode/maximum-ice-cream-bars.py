class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        count = 0
        sum_ = 0

        for i in range(len(costs)):
            if sum_ + costs[i] <= coins:
                count += 1
                sum_ += costs[i]
        return count



        