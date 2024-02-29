# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        position = head
        smallerDummy = ListNode()
        smaller = smallerDummy
        largerDummy = ListNode()
        larger = largerDummy

        while position:
            if position.val >= x:
                larger.next = ListNode(position.val)
                larger = larger.next
            elif position.val < x:
                smaller.next = ListNode(position.val)
                smaller = smaller.next
            position = position.next
        smaller.next = largerDummy.next

        return smallerDummy.next

        

        



            



        