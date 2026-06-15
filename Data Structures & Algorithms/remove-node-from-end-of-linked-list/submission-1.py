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

        prevNode = head
        nodePos = nodeCount - n
        nodeCount = 1
        if nodePos == 0:
            return head.next 
        while nodeCount != nodePos:
            nodeCount += 1
            prevNode = prevNode.next

        prevNode.next = prevNode.next.next

        return head