# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numArray = []
        temp = head
        while temp:
            numArray.append(temp.val)
            temp = temp.next
        l, r = 0, len(numArray) - 1
        while l <= r:
            if numArray[l] != numArray[r]:
                return False
            r-=1
            l+=1
        return True


        