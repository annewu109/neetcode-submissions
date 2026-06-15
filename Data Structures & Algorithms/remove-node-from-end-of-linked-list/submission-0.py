# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeCount = 0
        n1 = head
        while n1:
            nodeCount += 1
            n1 = n1.next

        prevNode = None
        nodeToRemove = head
        nodePos = nodeCount - n + 1
        nodeCount = 1
        while nodeToRemove and nodeCount != nodePos:
            nodeCount += 1
            prevNode = nodeToRemove
            nodeToRemove = nodeToRemove.next

        if not prevNode:
            return head.next
        else:
            prevNode.next = nodeToRemove.next

        return head