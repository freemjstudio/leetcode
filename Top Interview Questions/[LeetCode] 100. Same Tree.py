# https://leetcode.com/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150

'''


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q: # leaf node 에서 탐색 중지
            return True
        if not p or not q or p.val != q.val:
            return False
        if p.val == q.val: # 현재 노드 값이 같은 경우 left 와 right 또한 비교 시작
            return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))