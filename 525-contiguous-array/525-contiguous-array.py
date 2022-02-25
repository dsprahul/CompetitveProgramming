class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        from collections import defaultdict
        
        cum_sum = 0
        cum_arr = [0]
        for n in nums:
            if n == 0:
                cum_sum += 1
            else:
                cum_sum -= 1
                
            cum_arr.append(cum_sum)
            
        index = {}
        for idx, cn in enumerate(cum_arr, -1):
            if index.get(cn) == None:
                index[cn] = [idx, idx]
            else:
                index[cn][1] = idx
                
        max_len = -float("inf")
        for i, j in index.values():
            if j - i > max_len:
                max_len = j - i
                
        return max_len
    
                