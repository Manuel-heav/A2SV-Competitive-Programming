class Solution:
    def longestPalindrome(self, s: str) -> int:
        listArr = list(s)
        listCount = Counter(listArr)
        count = 0
        for item, value in listCount.items():
            if value % 2 == 0:
                count += value
            else:
                count += value - 1
                listCount[item] -= value - 1
        if 1 in listCount.values():
            count += 1
        return count
        