class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        
        out = []
        for idx, n in enumerate(nums):
            if n > 0:
                out.append(idx + 1)
                
        return out
            