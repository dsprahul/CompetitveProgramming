class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        from collections import Counter
        
        if k == 0:
            ans = 0
            for k, v in dict(Counter(nums).most_common()).items():
               if v > 1:
                    ans +=1
            
            return ans
        
        else:
            nums = set(nums)
            ans = set()
            for i in nums:
                if i + k in nums:
                    ans.add(tuple(sorted((i, (i + k)))))
            
            return len(ans)