# https://leetcode.com/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = 100000
        diff = 200000

        def inorder(root):
            nonlocal diff, prev

            if not root:
                return
            inorder(root.left)
            diff = min(diff, abs(root.val - prev))
            prev = root.val
            inorder(root.right)

        inorder(root)
        return diff