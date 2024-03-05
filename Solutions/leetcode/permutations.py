class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        bucket = []
        answer = []

        def backtrack(i):
            if len(nums) == len(bucket):
                answer.append(bucket[:])
                return 

            for j in range(len(nums)):
                if nums[j] not in bucket:
                    bucket.append(nums[j])
                    backtrack(j)
                    bucket.pop()
        backtrack(0)
        return answer


        