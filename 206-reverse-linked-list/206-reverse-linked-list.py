# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recCall(head, tailEnd):
        
            if head is None or head.next is None:
                return None, head

            pointer, tailEnd = recCall(head.next, tailEnd)
            
            tail = pointer or tailEnd
            tail.next = head
            head.next = None
        
            return tail.next, tailEnd
        
        _, tailEnd = recCall(head, None)
        
        return tailEnd
        
        
        