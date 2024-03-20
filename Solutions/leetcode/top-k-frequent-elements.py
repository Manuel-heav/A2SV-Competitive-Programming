class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        range_ = max(nums) - min(nums)
        counter = Counter(nums)
        ans = []       
        sortedArr = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            ans.append(sortedArr[i][0])
        return ans

        
        






        