class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        perimeter = 0
        N = len(nums) - 2
        for i in range(N):
            sideOne = nums[i]
            sideTwo = nums[i+1]
            sideThree = nums[i+2]

            if sideOne < sideThree + sideTwo:
                perimeter = sideOne + sideTwo + sideThree
                return perimeter

        return 0
            


        
        