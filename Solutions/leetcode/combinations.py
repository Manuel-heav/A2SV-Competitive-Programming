class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        bucket = []

        def backtrack(i):
            if len(bucket) == k:
                answer.append(bucket[::])
                return

            for j in range(i+1, n+1):
                bucket.append(j)
                backtrack(j)
                bucket.pop()
        backtrack(0)
        return answer        
        