class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        
        # Step 1: find first decreasing element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            
            # Step 2: find next greater element
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: reverse the remaining part
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1