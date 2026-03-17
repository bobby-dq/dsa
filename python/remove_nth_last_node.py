"""
PROBLEM: REMOVE NTH NODE FROM END OF LIST

Statement:
Given the head of a singly linked list and an integer 'n', remove the 
nth node from the end of the list and return the head of the modified list.

Constraints:
- The number of nodes (k) is 1 <= k <= 10^3
- -10^3 <= Node.value <= 10^3
- 1 <= n <= k

Technique: Two Pointers (Fast & Slow)
Time Complexity: O(k) - Single pass
Space Complexity: O(1) - Constant extra space
"""

# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode

def remove_nth_last_node(head, n):
    lpt = head
    rpt = head

    for i in range(n):
        rpt = rpt.next
    
    if not rpt:
        return head.next
    
    while rpt.next:
        rpt = rpt.next
        lpt = lpt.next

    lpt.next = lpt.next.next

    return head

