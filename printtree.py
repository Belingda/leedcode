# -*- coding:utf-8 -*-
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# 返回从上到下每个节点值列表，例：[1,2,3]
	def PrintFromTopToBottom(self, root):
		if root is None:
			return []
		tempnode = []
		tempnode.append(root)
		valres = []
		while (len(tempnode) > 0):
			node = tempnode.pop(0)
			valres.append(node.val)
			if node.left is not None:
				tempnode.append(node.left)
			if node.right is not None:
				tempnode.append(node.right)
		return valres
