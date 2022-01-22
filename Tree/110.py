# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(root: [TreeNode]) -> int:
            if root:
                left_depth = traverse(root.left)
                right_depth = traverse(root.right)
                if (abs(left_depth - right_depth)>1):
                    isB = False
                return max(left_depth, right_depth)+1
            else:
                return 0
            
        if root:
            isB = True
            traverse(root)
            return isB
        else: return True
