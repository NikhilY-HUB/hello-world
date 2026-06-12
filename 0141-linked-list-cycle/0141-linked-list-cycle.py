# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited_nodes = set()
        current = head

        while current is not None:
            if current in visited_nodes:
                return True
                
            visited_nodes.add(current)

            current = current.next
        return False