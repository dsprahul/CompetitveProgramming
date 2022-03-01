class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Init decision boundary index values
        upper = 0
        lower = len(matrix) - 1
        
        inner = 0
        outer = len(matrix[0]) - 1
        
        i, j = 0, 0
        m, n = len(matrix), len(matrix[0])
        
        
        
        output = []
        output.append(matrix[i][j])
        while upper <= lower and inner <= outer:
            
            
            
            # upper            
            while j < outer:
                j += 1
                output.append(matrix[i][j]) 
            upper += 1
                
            # outer
            if upper <= lower and inner <= outer:
                while i < lower:
                    i += 1
                    output.append(matrix[i][j])
                outer -= 1
            
            # lower
            if upper <= lower and inner <= outer:
                while j > inner:
                    j -= 1
                    output.append(matrix[i][j])                
                lower -= 1
            
            # inner
            if upper <= lower and inner <= outer:
                while i > upper:
                    i -= 1
                    output.append(matrix[i][j])
                inner += 1

        return output
                