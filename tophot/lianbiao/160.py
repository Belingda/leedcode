# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
		if not headA or not headB:
			return None
		nodeset = set()
		while(headA):
			nodeset.add(headA)
			headA = headA.next
		while(headB):
			if headB in nodeset:
				return headB
			else:
				headB = headB.next
		return None

