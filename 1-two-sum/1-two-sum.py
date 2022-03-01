class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_idx = {num: idx for idx, num in enumerate(nums)}
        
        for idx, num in enumerate(nums):
            if num_idx.get(target - num) not in [None, idx]:
                return [idx, num_idx[target - num]]