# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        first = temp

        while n >= 0:
            first = first.next
            n -= 1
        
        second = temp
        while first:
            second = second.next
            first = first.next
        if second and second.next:
            second.next = second.next.next

        return temp.next
        



        