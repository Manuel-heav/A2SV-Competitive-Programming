class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        bucket = []

        def backtrack(i):
            if len(bucket) == k and sum(bucket) == n:
                answer.append(bucket[::])
                return

            for j in range(i+1, 10):
                if sum(bucket) < n:
                    bucket.append(j)
                    backtrack(j)
                    bucket.pop()
        backtrack(0)
        return answer