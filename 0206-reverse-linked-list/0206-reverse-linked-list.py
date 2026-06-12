# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next #Looks ahead and pins next node to it's position

            curr.next = prev #breaks the link and reverses the allignment

            prev = curr #Sets the anchor to current node

            curr = next_node #Points to next node which is to be reversed, this will go on 
                             #until out next_node falls off the edge
                                        
        return prev