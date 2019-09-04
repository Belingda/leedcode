# -*- coding:utf-8 -*-
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def TreeDepth(self, pRoot):
		# write code here
		if pRoot is None:
			return 0
		tempnode = []
		tempnode.append(pRoot)
		nextcnt = 1
		nowlevel = 0
		depth = 0
		while (len(tempnode) > 0):
			node = tempnode.pop(0)
			nowlevel +=1 # 当前层次数目
			if node.left != None:
				tempnode.append(node.left)
			if node.right !=None:
				tempnode.append(node.right)
			if nowlevel == nextcnt:
				nowlevel = 0
				nextcnt = len(tempnode)
				depth +=1
		return depth


