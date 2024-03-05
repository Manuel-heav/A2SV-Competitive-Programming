# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        even = ListNode()
        odd = ListNode()

        e = even
        o = odd

        temp = head

        while temp:
            if counter % 2 == 0:
                o.next = ListNode(temp.val)
                o = o.next
                temp = temp.next
                counter += 1
            else:
                e.next = ListNode(temp.val)
                e = e.next
                temp = temp.next
                counter += 1
        o.next = even.next
        return odd.next
        