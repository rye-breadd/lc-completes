# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        def merge_list(l1, l2):
            res = ListNode()
            dummy = res
            
    
            c1 = l1
            c2 = l2
            while c1 and c2:
                c1_next = c1.next
                c2_next = c2.next

                if c1.val < c2.val:
                    dummy.next = c1
                    c1 = c1_next
                else:
                    dummy.next = c2
                    c2 = c2_next
                
                dummy = dummy.next
            
            if c1:
                dummy.next = c1
            else:
                dummy.next = c2
            
            return res.next

        while len(lists) >= 2:
            l1 = lists.pop()
            l2 = lists.pop()
            new_ll = merge_list(l1, l2)

            lists.append(new_ll)

        return lists[0]

            
        