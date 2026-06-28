# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Find the middle and split into two lists using slow and fast pointers
reverse the right one
merge the two linked lists into one 
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        prev = None
        slow = fast = head 
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # split the list (right side always smaller)
        temp = slow.next 
        slow.next = None
        slow = temp
        
        # reverse right side
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp 

        p1, p2 = head, prev
        while p2:
            t1, t2 = p1.next, p2.next
            p1.next = p2
            p2.next = t1
            p1, p2 = t1, t2
            


            




        


        
            
