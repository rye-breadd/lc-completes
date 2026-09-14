# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1 -> 2 -> 3
3 -> 2 -> 1

3 -> 2 -> 1

dummy <- 1 2 -> 3
dummy <- 1 <- 2 3

swap current
keep the next
go the the next --> current
swap the current
keep the next

dummy <- 1  <- 2 <- 3
prev = 3
curr = None
temp = None


"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
            
            

        
        