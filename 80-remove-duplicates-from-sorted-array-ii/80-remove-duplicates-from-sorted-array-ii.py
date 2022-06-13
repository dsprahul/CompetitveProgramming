class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        arr_length = len(nums)
        max_count = 2
        
        srt, cnt = 1, 1
        cur_count = 1
        while cnt < len(nums):
            
            if nums[cnt] == nums[cnt-1]:
                cur_count += 1
            else:
                cur_count = 1
                
            if cur_count <= max_count:
                nums[srt] = nums[cnt]
                cnt += 1
                srt += 1
            else:
                cnt += 1

            
        # Drop extra elements
        while srt < arr_length:
            nums.pop()
            srt += 1

            
        