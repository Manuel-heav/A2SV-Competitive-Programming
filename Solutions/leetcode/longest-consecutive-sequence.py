class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        noRep = list(set(nums))
        noRep.sort()
        answer = 0
        counter = 0
        for i in range(len(noRep)-1):
            if noRep[i+1] - noRep[i] == 1:
                counter += 1
            else:
                answer = max(counter, answer)
                counter = 0
        answer = max(counter, answer)
        return answer + 1


        