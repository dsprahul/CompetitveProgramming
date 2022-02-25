class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start_idx, end_idx = -1, -1
        
        if len(nums) == 0:
            return [-1, -1]
        
        low = 0
        high = len(nums) - 1
        
        while low <= high: # Find start_idx
            
            mid = (low + high) // 2
            
            if nums[mid] == target and (mid == 0 or nums[mid] > nums[mid - 1]):
                start_idx = mid
                break
                
            elif target <= nums[mid]:
                high = mid - 1
                
            else:
                low = mid + 1
                
                
        low = 0
        high = len(nums) - 1
        
        while low <= high: # Find end_idx
            
            mid = (low + high) // 2
            
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid] < nums[mid + 1]):
                end_idx = mid
                break
                
            elif target >= nums[mid]:
                low = mid + 1
                
            else:
                high = mid - 1
                
        return [start_idx, end_idx]
                
            