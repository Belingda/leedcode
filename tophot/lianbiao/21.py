# https://leetcode-cn.com/problems/merge-two-sorted-lists/
# 21Ìâ
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		pre = ListNode(-1)
		head = pre
		while(l1 and l2):
			if (l1.val <= l2.val):
				pre.next = l1
				l1 = l1.next
				pre = pre.next
			elif (l2.val <= l1.val):
				pre.next = l2
				l2 = l2.next
				pre = pre.next
		while(l1):
			pre.next = l1
			l1 = l1.next
			pre = pre.next
		while(l2):
			pre.next = l2
			l2 = l2.next
			pre = pre.next
		return head.next