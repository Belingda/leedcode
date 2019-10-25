# -*- coding:utf-8 -*-
import test1
"""
二叉树中和为某一值的路径
"""
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# 返回二维列表，内部每个列表表示找到的路径
	def FindPath(self, root, expectNumber):
		return self.RealFindPath(root, 0, expectNumber, [], [])

	def RealFindPath(self, root, sum, expectNumber, path, allpath):
		if root is None:
			return allpath
		sum += root.val
		path.append(root.val)
		if root.left is None and root.right is None:
			if sum == expectNumber:
				allpath.append(path[:])
		if root.left:
			self.RealFindPath(root.left, sum, expectNumber, path, allpath)
		if root.right:
			self.RealFindPath(root.right, sum, expectNumber, path, allpath)
		# 回退到上个结点前弹出当前元素
		if len(path) > 0:
			num = path.pop()  # 弹出末尾元素
			sum = sum - num
		return allpath

class Solution2:
	# 返回二维列表，内部每个列表表示找到的路径
	def FindPath(self, root, expectNumber):
		return self.RealFindPath(root, expectNumber, [], [])

	def RealFindPath(self, root, expectNumber, path, allpath):
		if root is None:
			return allpath
		expectNumber -=root.val
		path.append(root.val)
		if root.left is None and root.right is None:
			if expectNumber == 0:
				allpath.append(path[:])
		if root.left:
			self.RealFindPath(root.left, expectNumber, path, allpath)
		if root.right:
			self.RealFindPath(root.right, expectNumber, path, allpath)
		if len(path) > 0:
			path.pop()  # 弹出末尾元素
		return allpath