# https://leetcode.com/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = int(1e9)
        answer = int(1e9) # diff
        def inorder(root): # inorder 로 해야 오름차순 순회 가능
            if root is None:inorder(0)
                return # exit
            # left
            inorder(root.left)
            # root -> 여기서 값 비교하기
            answer = min(answer, root.value - prev)
            # right
            inorder(root.right)
        return answer