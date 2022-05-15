class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        nums.sort()
        answers = []
        
        n = len(nums)
        i = 0
        while i < n - 2:
            
            j = i + 1
            k = n - 1
            while j < k:
                
                
                triplet = (nums[i], nums[j], nums[k])
                if sum(triplet) < 0:
                    j += 1
                    while 0 < j < k < n-1 and nums[j] == nums[j - 1]:
                        j += 1
                    
                elif sum(triplet) > 0:
                    k -= 1
                    while 0 < j < k < n-1 and nums[k] == nums[k + 1]:
                        k -= 1
                        
                else:
                    answers.append(triplet)
                    j += 1
                    while 0 < j < k < n-1 and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while 0 < j < k < n-1 and nums[k] == nums[k + 1]:
                        k -= 1
            
            i += 1
            while i < n-2 and nums[i] == nums[i - 1]:
                i += 1
                    
        return answers