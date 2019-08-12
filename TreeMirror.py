# -*- coding:utf-8 -*-
'''
	树的镜像
	思路：递归交换左右结点
'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# 返回镜像树的根节点
	def Mirror(self, root):
		# write code here
		if root is None:
			return root
		if root.left is None and root.right is None:
			return root
		tempNode = root.left
		root.left = root.right
		root.right = tempNode
		self.Mirror(root.left)
		self.Mirror(root.right)
