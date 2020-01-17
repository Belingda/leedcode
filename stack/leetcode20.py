# -*- coding: gbk -*-

class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		symbolend = {'}': '{',
		     ']': '[',
		     ')': '(',
		     }
		tempstack=[]
		for v in s:
			if v not in symbolend:
				tempstack.append(v)
			else:
				if len(tempstack) == 0:
					return False
				if tempstack[-1] != symbolend[v]:
					return False
				tempstack.pop()
		return True if len(tempstack) == 0 else False
