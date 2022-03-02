class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        from itertools import product
        from copy import deepcopy
        
        board_copy = deepcopy(board)
        
        m, n = len(board), len(board[0])
        
        def get_n_live_neighbors(i, j):
            
            neighbors_vals = [
                lambda i, j: board_copy[i-1][j-1] if i - 1 >= 0 and j - 1 >= 0 else 0,
                lambda i, j: board_copy[i-1][j] if i - 1 >= 0 else 0,
                lambda i, j: board_copy[i-1][j+1] if i - 1 >= 0 and j + 1 < n else 0,
                lambda i, j: board_copy[i][j-1] if j - 1 >= 0 else 0,
                lambda i, j: board_copy[i][j+1] if j + 1 < n else 0,
                lambda i, j: board_copy[i+1][j+1] if i + 1 < m and j + 1 < n else 0,
                lambda i, j: board_copy[i+1][j] if i + 1 < m else 0,
                lambda i, j: board_copy[i+1][j-1] if i + 1 < m and j - 1 >= 0 else 0
            ]
            
            return sum([fn(i, j) for fn in neighbors_vals])
            
        for i, j in product(range(m), range(n)):
            
            n_live = get_n_live_neighbors(i, j)
            
            if board[i][j] == 1 and (n_live < 2 or n_live > 3):
                board[i][j] = 0
                
            elif board[i][j] == 0 and n_live == 3:
                board[i][j] = 1
                
                    
            
            
            
            