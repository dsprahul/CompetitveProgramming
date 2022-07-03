# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        answer = True
        
        def inOrder(root, prev, ans):

            if not root:
                return prev, ans
            
            prev, ans = inOrder(root.left, prev, ans)
                        
            if not (prev < root.val):
                ans *= False
            
            prev = root.val
            prev, ans = inOrder(root.right, prev, ans)
            
            return prev, ans
            
        _, answer = inOrder(root, -float("inf"), answer)
        
        return answer
            