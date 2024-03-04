class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0]*k
        curr = float("inf")
        def backtrack(i, bucket):
            nonlocal curr
            if i == len(cookies):
                curr = min(curr, max(bucket))
                return
            if max(bucket) > curr:
                return 
 
            for j in range(k):
                bucket[j] += cookies[i]
                backtrack(i+1, bucket)
                bucket[j] -= cookies[i]
        backtrack(0, bucket)
        return curr

            

        