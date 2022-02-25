class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # nums sorted n times
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]

        low = 0
        high = len(nums) - 1
        while low <= high:
            
            mid = (low + high) // 2
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            elif nums[mid - 1] < nums[high]:
                high = mid - 1
                
            else:
                low = mid + 1