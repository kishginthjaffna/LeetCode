# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def get_length(self, current):
        count = 0
        while current.next:
            count += 1
            current = current.next
        return count

    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        len = self.get_length(current)
        count = 0
        while current.next:
            if count == len - n:
                current.next = current.next.next
            else:
                current = current.next
            count += 1
        return dummy.next

        
        