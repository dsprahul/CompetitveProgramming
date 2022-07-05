# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        
        def dfs(root, agg):
            
            if root.left is None and root.right is None:
                agg = agg * 10 + root.val 
                
                nonlocal total
                total += agg
                return
            
            agg = agg * 10 + root.val 
            if root.left:
                dfs(root.left, agg)
            if root.right:
                dfs(root.right, agg)
            
        dfs(root, 0)
        
        return total
            
                
                
            
                