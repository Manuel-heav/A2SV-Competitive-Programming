class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boat = len(people)

        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                boat -= 1
            else:
                right -= 1
        
        return boat


