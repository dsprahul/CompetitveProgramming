# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        answer = True
        prev = -float("inf")
        
        def inOrder(root):
            
            nonlocal prev
            nonlocal answer
            if not root:
                return
            
            inOrder(root.left)
                        
            if not (prev < root.val):
                answer = False
            
            prev = root.val
            inOrder(root.right)
            
        inOrder(root)
        
        return answer
            