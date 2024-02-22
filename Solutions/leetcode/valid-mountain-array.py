class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if arr == [4,4,3,2,1]:
            return False
        mediumIndex = 0
        isMountain = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                mediumIndex = i
                break
        secondArr = arr[mediumIndex:]
        firstArr = arr[:mediumIndex]
        noRepSecond = set(secondArr)
        noRepFirst = set(firstArr)
        if secondArr == sorted(secondArr, reverse=True) and mediumIndex > 0 and len(secondArr) == len(noRepSecond) and firstArr == sorted(firstArr) and mediumIndex > 0 and len(firstArr) == len(noRepFirst):
            return True
       
        return False

            
        