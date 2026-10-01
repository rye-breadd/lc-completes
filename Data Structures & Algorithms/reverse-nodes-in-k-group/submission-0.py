# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""

slow and fast pointer for delay
    edge case: what if we hit the end = then we revese the linkedlist from there
helper func to reverse the current sublinkedlist



head = 1, 2, 3, 4      k = 2

dummy = None 1 2 3 4
slow = None
fast = 4

node = 3
prev = 2
temp = 3

None -> 2 -> 1 -> 3 -> 4 -> None
"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_nodes(fast_next, slow):
            node = slow.next
            prev = fast_next
            while node != fast_next:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            slow.next = prev

        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast.next: 
            c = k
            while c > 0 and fast.next:
                fast = fast.next
                c -= 1
            
            # edge case end
            if c > 0:
                return dummy.next

            begin = slow.next
            reverse_nodes(fast.next, slow)

            slow, fast = begin, begin

        return dummy.next
    
    



                
            

        


        
        