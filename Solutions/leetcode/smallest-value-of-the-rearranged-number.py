class Solution:
    def smallestNumber(self, num: int) -> int:
        numList = list(map(str, str(num)))
        if num > 0:
            numList.sort()
            zero = numList.count("0")
            updated = [x for x in numList if x != "0"]
            for i in range(zero):
                updated.insert(1+i, "0")
            return int("".join(updated))
        elif num < 0:
            updated = numList[1:]
            updated.sort(reverse=True)
            return int("".join(updated)) * -1
        else:
            return 0


    
        