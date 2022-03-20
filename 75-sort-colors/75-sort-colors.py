class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        sorter = 0
        runner = 0
        
        current_color = 0
        
        while sorter < n - 1:
            
            # Reset bubbled/runner after each runner pass
            runner = sorter
            
            # First unsorted ball
            if nums[sorter] != current_color:
                
                while runner < n:
                    # Discovered a element that should be at current sorter
                    if nums[runner] == current_color:
                        bubble = True
                        break    
                    runner += 1
                else:
                    bubble = False
                    current_color += 1
                    
                # bubble things to right by one place
                if bubble:
                    while runner > sorter:
                        nums[runner] = nums[runner - 1]
                        runner -= 1
                    nums[runner] = current_color
                    sorter += 1


            else:
                sorter += 1

            