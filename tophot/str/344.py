# -*- coding: gbk -*-
# 翻转字符串
class Solution:
	def reverseString(self, s) -> None:
		"""
		Do not return anything, modify s in-place instead.
		"""
		length = len(s)
		left = 0
		right = int((length-1))
		while(left < right):
			temp = s[left]
			s[left] = s[right]
			s[right] = temp
			left +=1
			right -=1
		return s