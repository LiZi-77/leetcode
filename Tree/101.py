# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(l: Optional[TreeNode], r: Optional[TreeNode]):
            if l is None and r is None: return True
            elif l is None or r is None: return False
            elif l.val != r.val: return False
            else: return check(l.right,r.left) and check(l.left, r.right)
        
        if root is None: return True
        return check(root.left, root.right)
    
