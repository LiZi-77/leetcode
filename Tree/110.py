# Definition for a binary tree node. 失败答案！
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

# Definition for a binary tree node. 成功答案
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(r: Optional[TreeNode]) -> int:
            if r:
                left_depth = depth(r.left)
                right_depth = depth(r.right)
                
                return max(left_depth,right_depth)+1
            else: return 0
            
        if root:
            l = depth(root.left)
            r = depth(root.right)
            balance = (abs(l - r) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)
            return balance
        else:
            return True
