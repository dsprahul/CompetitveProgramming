class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums = set(nums)
        out = []
        for i in range(1, n + 1):
            if i not in nums:
                out.append(i)
                
        return out
            