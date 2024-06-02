"""
1. Add Two Numbers

https://leetcode.com/problems/add-two-numbers/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.
        """
        ans = ListNode()
        curr = ans
        carry = 0

        # Loop while there are still nodes to add
        while l1 != None or l2 != None or carry != 0:

            # Get current node values if node exists 
            l1_val = l1.val if l1 != None else 0
            l2_val = l2.val if l2 != None else 0

            total = l1_val + l2_val + carry
            carry = total // 10

            newNode = ListNode(total % 10)

            curr.next = newNode                        
            curr = curr.next
            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2
        
        # Return the next node of the answer so that it does not include the first node set to 0
        return ans.next


if __name__ == "__main__":
    # Testes
    s = Solution()
    ans =  s.addTwoNumbers(
        ListNode(2, next=ListNode(4, next=ListNode(3))), 
        ListNode(5, next=ListNode(6, next=ListNode(4))))
    assert ans.val == 7
    assert ans.next.val == 0
    assert ans.next.next.val == 8
    assert ans.next.next.next == None

    ans2 = s.addTwoNumbers(ListNode(0), ListNode(0))
    assert ans2.val == 0
    assert ans2.next == None
