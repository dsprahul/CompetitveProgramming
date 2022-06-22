# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(val=-10**5)
        dummy.next = head
        
        slow, fast = dummy, dummy
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                slow = dummy
                while slow is not fast:
                    fast = fast.next
                    slow = slow.next
                    
                return slow
        return None
        
            
            
            