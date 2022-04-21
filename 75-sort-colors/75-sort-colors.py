class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n0, n1, n2 = 0, 0, 0
        
        for i in nums:
            if i == 0:
                n0 += 1
            elif i == 1:
                n1 += 1
            else:
                n2 += 1
                
        for i in range(len(nums)):
            if i < n0:
                nums[i] = 0
            elif n0 <= i < n0 + n1:
                nums[i] = 1
            else:
                nums[i] = 2
            