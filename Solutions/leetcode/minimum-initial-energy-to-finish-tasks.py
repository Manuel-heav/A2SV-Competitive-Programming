class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])

        answer = 0
        for a,b in tasks:
            answer += a
        result = answer
        for a, b in tasks:
            if b > result:
                 answer += b - result
                 result = b
                
            result -= a
                
        return answer