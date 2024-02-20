class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : -abs(x[0] - x[1]))
        b = a = len(costs)/2
        total = 0
        for aCost, bCost in costs:
            if b == 0 or (a > 0 and aCost <= bCost):
                total += aCost
                a -= 1
            else:
                total += bCost
                b -= 1
        return total