# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        binary_str = ""
        current = head

        while current != None:
            binary_str += str(current.val)
            current = current.next
        return int(binary_str, 2)