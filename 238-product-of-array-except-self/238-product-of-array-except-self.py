class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        def cum_prod(nums):
            prod = []
            running_prod = 1
            for num in nums:
                prod.append(num * running_prod)
                running_prod *= num
                
            return prod
        lprod = cum_prod(nums)
        rprod = cum_prod(nums[::-1])[::-1]
        
        ans = []
        for i in range(len(nums)):
            
            if i == 0:
                ans.append(rprod[1])
                
            elif i == len(nums) -1:
                ans.append(lprod[-2])
                
            else:
                ans.append(lprod[i-1] * rprod[i+1])
                
        return ans
                
            
            