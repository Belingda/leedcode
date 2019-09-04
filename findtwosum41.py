# -*- coding:utf-8 -*-


class Solution:
	def FindNumbersWithSum(self, array, tsum):
		# write code here
		if array is None or len(array) <2 :
			return []
		front = 0
		end = len(array) - 1
		while (front < end):
			if array[front] + array[end] == tsum:
				return array[front],array[end]
			if array[front] + array[end] < tsum:
				front += 1
			if array[front] + array[end] > tsum:
				end -= 1
		return []