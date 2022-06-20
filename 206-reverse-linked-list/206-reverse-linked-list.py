# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        prev, curr, fast = head, head.next, head.next.next
        head.next = None
        while fast:
            
            curr.next = prev
            
            prev, curr, fast = curr, fast, fast.next
            
        curr.next = prev
        
        return curr