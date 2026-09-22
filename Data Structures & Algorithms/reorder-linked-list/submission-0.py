# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

None <- 6 8 10

temp = node.next
node.next = None
prev = node
node = temp


"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid first
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None
        
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        left = head
        right = prev

        
        while left and right:
            lt = left.next
            rt = right.next

            left.next = right
            right.next = lt
            left = lt
            right = rt
            
            
        



        