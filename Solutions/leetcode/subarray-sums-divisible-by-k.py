class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        counter = {0:1}
        
        for n in nums:
            prefix_sum += n
            res = prefix_sum % k
            if res in counter:
                count += counter[res]
                counter[res] += 1
            else:
                counter[res] = 1
                
        return count