class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        n, m = len(mat), len(mat[0])
        i, j = 0, 0
        direction = 1
        output = []
        
        for _ in range(m * n):
            
            output.append(mat[j][i])
            
            if direction == 1:
                
                if i == m - 1:
                    j += 1
                    direction = -1
                elif j == 0:
                    i += 1
                    direction = -1
                else:
                    i += 1
                    j -= 1
                    
            elif direction == -1:
                
                if j == n - 1:
                    i += 1
                    direction = 1
                elif i == 0:
                    j += 1
                    direction = 1
                else:
                    i -= 1
                    j += 1
                
                
        return output
                
        