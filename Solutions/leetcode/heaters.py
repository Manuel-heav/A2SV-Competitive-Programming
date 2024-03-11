class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def checker(num):
            house, heater = 0, 0 
            while house < len(houses) and heater < len(heaters):
                if abs(houses[house] - heaters[heater]) > mid:
                    heater += 1
                else:
                    house += 1
            if house == len(houses):
                return True
            return False
        
        low = 0
        high = max(max(houses), max(heaters))

        while low <= high:
            mid = (low + high)//2
            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

