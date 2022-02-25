class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Search for possible row
        low = 0
        high = len(matrix) - 1
        
        
        while True:
            mid = ( high + low ) // 2
            
            if target > matrix[mid][-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            elif matrix[mid][0] <= target <= matrix[mid][-1]:
                target_i = mid
                break
                
            if high < low:
                return False
        print(target_i)         
        
        # Search for possible col
        low = 0
        high = len(matrix[0]) - 1
        
        
        while True:
            mid = (high + low) // 2
            
            if target == matrix[target_i][mid]:
                return True
            
            elif target > matrix[target_i][mid]:
                low = mid + 1
            else:
                high = mid - 1
                
            if high < low:
                return False 

            