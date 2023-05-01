# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        pointer = answer
        ten = 0

        while (l1 or 12 or ten):
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            total = num1 + num2
            new_num = total % 10
            ten = total // 10  # 10의 자리수
            pointer.next = ListNode(new_num)
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return answer.next