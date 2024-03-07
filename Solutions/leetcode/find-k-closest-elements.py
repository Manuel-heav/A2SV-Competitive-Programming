class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        ans = []
        left = idx - 1
        right = idx 
        while k: 
            if left >= 0 and right < len(arr):
                a = abs(arr[right] - x)
                b = abs(x - arr[left])
                if a >= b:
                    ans.append(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
            elif left >= 0:
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
            
            k -= 1
        ans.sort()
        return ans

        



            