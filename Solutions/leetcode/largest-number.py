class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a,b):
            if str(a) + str(b) < str(b) + str(a):
                return 1
            elif str(a) + str(b) == str(b) + str(a):
                return 0
            else:
                return -1
        nums.sort(key=cmp_to_key(compare))

        if all(i == 0 for i in nums):
            return "0"
        else:
            return "".join(str(i) for i in nums)
        