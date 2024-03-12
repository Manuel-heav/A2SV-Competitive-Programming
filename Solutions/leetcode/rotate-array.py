class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        nums[k:] = reversed(nums[k:])
        nums[:k] = reversed(nums[:k])
        

# Let the array be - 123456789 and k = 4

# Step 1 - 12345 6789 ---> 54321 6789

# Step 2 - 54321 6789 ---> 54321 9876

# Step 3 - 543219876 ---> 678912345