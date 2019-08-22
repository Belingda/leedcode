# -*- coding:utf-8 -*-
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def isSymmetrical(self, pRoot):
		# write code here
		if pRoot is None:
			return True
		return self.IsRealSymmetrical(pRoot.left, pRoot.right)

	def IsRealSymmetrical(self, Lroot, Rroot):
		if (Lroot and Rroot is None) or (Rroot and Lroot is None):
			return False
		if Lroot is None and Rroot is None:
			return True
		if Lroot.val != Rroot.val:
			return False
		return self.IsRealSymmetrical(Lroot.left, Rroot.right) and self.IsRealSymmetrical(Lroot.right, Rroot.left)


