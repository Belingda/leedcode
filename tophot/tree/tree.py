# -*- coding: gbk -*-
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# 二叉树的最大深度
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
	def maxDepth(self, root: TreeNode) -> int:
		if root is None:
			return 0
		a= self.maxDepth(root.left)
		b = self.maxDepth(root.right)
		return a+1 if a>b else b+1

class Solution2:
	def maxDepth(self, root: TreeNode) -> int:
		if not root:
			return 0
		queue = [(root,1)]
		maxdepth = 1
		while(queue):
			nodedata = queue.pop()
			node,nodedepth = nodedata
			maxdepth = max(maxdepth,nodedepth)
			if node.left:
				queue.append((node.left,nodedepth+1))
			if node.right:
				queue.append((node.right,nodedepth+1))
		return maxdepth

# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 二叉搜索树 左中右 可得有序序列
class Solution3:
	def sortedArrayToBST(self, nums) -> TreeNode:
