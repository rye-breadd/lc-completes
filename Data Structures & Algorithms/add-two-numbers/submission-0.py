# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""

"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def calc_sum(head):
            c = 1
            total = 0

            dummy = head
            while dummy:
                curr_val = dummy.val
                curr_val *= c
                
                total += curr_val
                c *= 10
                dummy = dummy.next
            
            return total

        total_str = str(calc_sum(l1) + calc_sum(l2))
        res = ListNode()
        dummy = res
        for i in range(len(total_str) - 1, - 1, -1):
            dummy.next = ListNode(val=int(total_str[i]))
            dummy = dummy.next
        
        return res.next

"""
l1=[1,2,3]
l2=[4,5,6]

calc_sum l1
c = 1000
total = 321
dummy = None
curr_val = 300

"975"

None -> 5 -> 7 -> 9



"""
    
                

        