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

    def middleNode(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        dummy2 = ListNode(0)

        len = self.get_length(current)
        mid = len // 2
        count = 0
        while current.next:
            if count == mid:
                head = current.next
                break
            else:
                current = current.next
            count+=1
        return head







        