# -*- coding: gbk -*-

# 最长连续序列
# 未通过
class UnionFind(object):
	def __init__(self,data):
		self.m_Leaders = {}
		self.m_MaxLength = 0
		self.m_MaxFather = 0
		for node in data:
			self.m_Leaders[node] = node

	def FindLeader(self, node):
		tempnode = node
		paths = []
		tempmax = 1
		while (self.m_Leaders[tempnode] != tempnode):
			paths.append(tempnode)
			tempnode = self.m_Leaders[tempnode]
			tempmax +=1
		self.m_MaxLength = tempmax if tempmax > self.m_MaxLength else self.m_MaxLength
		for node in paths:
			self.m_Leaders[node] = tempnode


class Solution:
	def longestConsecutive(self, nums) -> int:
		ob = UnionFind(nums)
		for n in nums:
			if n in ob.m_Leaders and n+1 in ob.m_Leaders:
				ob.m_Leaders[n+1]= n
		print(ob.m_Leaders)
		for n in nums:
			ob.FindLeader(n)

		print(ob.m_Leaders)
		return ob.m_MaxLength

ob = Solution()
print(ob.longestConsecutive([-1,1,2,0]))