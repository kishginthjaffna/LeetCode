# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insert_at_end(self, data, head):
        if head is None:
            node = ListNode(data, None)
            return node
            
        itr = head
        while itr.next:
            itr = itr.next
        
        itr.next = ListNode(data, None)
        return head

    def create_list(self, head, array):
        head = None
        for data in array:
            head = self.insert_at_end(data, head)
        return head

    def reverseList(self, head):
        itr = head
        arr = []
        while itr:
            arr.append(itr.val)
            itr = itr.next
        return self.create_list(None, arr[::-1])
