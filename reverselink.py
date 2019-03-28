# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr,prev=head,None
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            if curr:
                print("curr%d"%curr.val)
        return prev
    def printList(self,head):
        curr=head
        while(curr):
            print(curr.val)
            curr=curr.next

node=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node.next=node2
node2.next=node3
ob=Solution()
ob.reverseList(node)
ob.printList(node3)