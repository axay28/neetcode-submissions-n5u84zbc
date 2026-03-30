# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,new=None,head
        while new:
            temp=new.next
            new.next=prev
            prev=new
            new=temp
        return prev