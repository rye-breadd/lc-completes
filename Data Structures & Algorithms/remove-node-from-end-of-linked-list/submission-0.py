# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
dummy [1,2,3,4]
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = ListNode()
        front.next = head
    
        dummy = head
        slow = front
        count = 0
        
        while count != n:
            count += 1
            dummy = dummy.next
        
        while dummy:
            slow = slow.next
            dummy = dummy.next
            
        slow.next = slow.next.next
            
        return front.next


        