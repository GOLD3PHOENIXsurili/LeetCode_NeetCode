# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next

        while cur:
            gcd  = math.gcd(cur.val, prev.val) # size A
            g = ListNode(gcd)
            prev.next = g
            g.next = cur
            prev = cur
            cur = cur.next
        return head

    # Time: O(n*A)
    # Space: O(1)
    