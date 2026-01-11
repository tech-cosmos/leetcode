# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        heap=[]
        for i,node in enumerate(lists):
            while node:
                heapq.heappush(heap,node.val)
                node=node.next
        while heap:
            val=heapq.heappop(heap)
            tail.next=ListNode(val)
            tail=tail.next
        
        tail.next=None
        return dummy.next