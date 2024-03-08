class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        num = 0

        for i in range(len(flips)):
            num = max(num, flips[i])
            if num == i+1:
                count += 1
        return count
        # flipper = [0] * len(flips)
        # counter = 0

        # for i in range(len(flips)):
        #     print(flipper[0:flips[i]])
        #     if flipper[0:flips[i]].count(1) == i+1:
        #         counter += 1
        #     flipper[flips[i]-1] = 1
        #     # print(flipper)
        # return counter