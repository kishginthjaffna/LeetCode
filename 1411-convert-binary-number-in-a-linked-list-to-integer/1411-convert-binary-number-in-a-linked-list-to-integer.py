# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def get_length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def getDecimalValue(self, head):
        num = 0
        length = self.get_length(head)
        itr = head
        
        while itr:
            length -= 1
            num += itr.val * (2 ** length)
            itr = itr.next
        return num
