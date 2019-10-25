# -*- coding:utf-8 -*-
'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
'''
	没有右子树
	左根右
	当前为父节点的左节点，则下一个结点为父节点
	当前为右结点，则下一个是父节点左结点 的父结点 
'''

class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
	def GetNext(self, pNode):
		if pNode is None:
			return None
		# 有右子树
		if pNode.right != None:
			while(pNode.left!=None):
				pNode = pNode.left
			return pNode
		if pNode.next and pNode.next.left == pNode:
			return pNode.next
		while(pNode.next):
			if pNode.next.left == pNode:
				return pNode.next
			pNode = pNode.next
		return pNode.next

'''
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''
class Solution1:
	def __init__(self):
		self.m_MinStack = []
		self.m_MyStack = []

	def push(self, node):
		if self.m_MinStack:
			if node < self.m_MinStack[-1]:
				self.m_MinStack.append(node)
			else:
				self.m_MinStack.append(self.m_MinStack[-1])
		else:
			self.m_MinStack.append(node)
		self.m_MyStack.append(node)

	def pop(self):
		if self.m_MinStack and self.m_MyStack:
			self.m_MinStack.pop()
			return self.m_MyStack.pop()

	def top(self):
		return self.m_MyStack[-1]

	def min(self):
		return self.m_MinStack[-1]


class Solution:
	# 返回[a,b] 其中ab是出现一次的两个数字
	def FindNumsAppearOnce(self, array):
		appearcnt = {}
		res = []
		for a in array:
			appearcnt[a] = appearcnt.get(a,0)+1
		for a,cnt in appearcnt.items():
			if cnt == 1:
				res.append(a)
		return res