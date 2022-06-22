# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        stack = []
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast is None:  # Even – slow head inclusive
            pass
        else:  # Odd – slow head exclusive
            slow = slow.next
        
        # prev = slow
        # slow = slow.next
        # prev.next = None

        while slow:
            stack.append(slow)
            slow = slow.next
            
        runner = head
        while stack:
            
            node_n = stack.pop()
            next_to_runner = runner.next
            runner.next = node_n
            node_n.next = next_to_runner
            runner = next_to_runner
            
        runner.next = None