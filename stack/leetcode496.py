# -*- coding: gbk -*-

# 单调栈
class Solution(object):
	def nextGreaterElement(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		tempstack = []
		nextmap = {}
		for n in nums2:
			if len(tempstack) == 0:
				tempstack.append(n)
			else:
				if n>tempstack[-1]:
					while (tempstack and n > tempstack[-1]):
						nextmap[tempstack[-1]] = n
						tempstack.pop()
				tempstack.append(n)

		for n in tempstack:
			nextmap[n] = -1
		res = []
		for n1 in nums1:
			res.append(nextmap[n1])
		return res

ob = Solution()
ob.nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7])


