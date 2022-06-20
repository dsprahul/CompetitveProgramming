# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        dummy = ListNode(val=-1, next=head)
        
        pt1, pt2 = dummy, dummy
        while pt1.next:
            
            pt1 = pt1.next
            n -= 1
            
            if n < 0:
                pt2 = pt2.next
            
        
        pt2.next = pt2.next.next
        
        return dummy.next
            
        