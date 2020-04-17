# -*- coding: gbk -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def middleNode(self, head: ListNode) -> ListNode:
		if not head:
			return head
		temp = head
		length = 0
		while (temp):
			temp = temp.next
			length += 1
		cnt = 0
		temp = head
		while (temp):
			cnt += 1
			if length %2 == 0 and cnt > (length / 2):
				return temp
			elif length %2 == 1 and cnt >= (length / 2):
				return temp

			temp = temp.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
ob=Solution()
print(ob.middleNode(node1).val)


# 快慢指针解法 快指针走2步 慢指针走1步 当快指针走完时，慢指针在中点
class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow