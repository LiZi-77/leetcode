# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==1: return TreeNode(nums[0])
        else:
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            l = mid - 1
            r = mid + 1
            
            if l < 0 :left_tree = None
            else: left_tree = self.sortedArrayToBST(nums[:mid])
                
            if r >= len(nums): right_tree = None
            else: right_tree = self.sortedArrayToBST(nums[r:])
            
            root.left = left_tree
            root.right = right_tree
            
            return root
