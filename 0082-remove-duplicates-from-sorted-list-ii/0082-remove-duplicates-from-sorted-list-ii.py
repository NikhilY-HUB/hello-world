# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy

        while slow.next != None and slow.next.next != None:
            if slow.next.val == slow.next.next.val:
                duplicate_val = slow.next.val
                fast = slow.next

                while fast != None and fast.val == duplicate_val:
                    fast = fast.next

                slow.next = fast

            else:
                slow = slow.next
        return dummy.next