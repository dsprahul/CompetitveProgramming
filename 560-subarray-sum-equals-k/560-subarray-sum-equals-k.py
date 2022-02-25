class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        from collections import defaultdict
        cum_arr = [0]
        cum_sum = 0
        for n in nums:
            
            cum_sum += n
            cum_arr.append(cum_sum)

        answer = 0
        index = defaultdict(int)
        for idx, n in enumerate(cum_arr):
            
            if index.get(n-k) != None:
                answer += index[n-k]     
            index[n] += 1
                
        return answer
        