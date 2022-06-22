# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        headA_nodes = set()
        
        while headA:
            headA_nodes.add(id(headA))
            headA = headA.next
            
        while headB:
            if id(headB) in headA_nodes:
                return headB
            headB = headB.next
            
        return None