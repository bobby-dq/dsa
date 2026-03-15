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

