# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = list1
        l2_head = list2
        
        res = ListNode()
        dummy = res

        while l1_head and l2_head:
            l1_next = l1_head.next
            l2_next = l2_head.next
            
            if l1_head.val < l2_head.val:
                dummy.next = l1_head
                l1_head = l1_next
            else:
                dummy.next = l2_head
                l2_head = l2_next
        
            dummy = dummy.next
        
        if l1_head:
            dummy.next = l1_head
        else:
            dummy.next = l2_head
        
        return res.next



            


        