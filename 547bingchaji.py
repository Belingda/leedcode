# -*- coding: gbk -*-

"""
{
	结点：结点父亲
}
"""
# List[List[int]]

# [
# [],
#[]
# ]

# [1]
class Solution:
	def findCircleNum(self, M):
		ob = UnionFind()
		for i in range(len(M)):
			ob.m_Leaders[i] = i
		for i in range(len(M)):
			for j in range(len(M[i])):
				if M[i][j] == 1 :
					if i != j:
						ob.Union(i, j)
					#print(ob.m_Leaders)
		return ob.GetCount()

class UnionFind(object):
	def __init__(self):
		self.m_Leaders = {}

	def FindLeader(self, node):
		if node not in self.m_Leaders:
			self.m_Leaders[node] = node
			return node
		tempnode = node
		paths = []
		# 2:1,1:3,3:3
		while (self.m_Leaders[tempnode] != tempnode):
			paths.append(tempnode)
			tempnode = self.m_Leaders[tempnode]
		for node in paths:
			self.m_Leaders[node] = tempnode
		return tempnode

	def IsSameSet(self,node1,node2):
		return self.FindLeader(node1) == self.FindLeader(node2)

	def Union(self,node1,node2):
		# rank的优化要看下
		fnode1 = self.FindLeader(node1)
		fnode2 = self.FindLeader(node2)
		if fnode1 != fnode2:
			self.m_Leaders[fnode1] = fnode2

	def GetCount(self):
		count = 0
		for node, leader in self.m_Leaders.items():
			if node == leader:
				count += 1
		return count

ob = Solution()
print(ob.findCircleNum([[1, 1, 1], [1, 1, 0], [1, 0, 1], ]))
