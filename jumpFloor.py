# -*- coding:utf-8 -*-
class Solution:
	def jumpFloor(self, number):
		if number <= 0:
			return 0
		if number == 1:
			return 1
		if number == 2:
			return 2
		res = [1, 2]
		for i in range(2, number):
			res.append(res[i - 1] + res[i - 2])
		return res[number - 1]

	def jumpFloor2(self, number):
		if number <= 0:
			return 0
		if number == 1:
			return 1
		if number == 2:
			return 2
		pre = 1
		cur = 2
		sum = pre + cur
		for i in range(3, number + 1):
			sum = pre + cur
			pre = cur
			cur = sum
		return sum


class Solution2:
	def Fibonacci(self, n):
		if n <= 0:
			return 0
		if n == 1:
			return 1
		if n == 2:
			return 1
		pre = 1
		cur = 1
		sum = pre + cur
		for i in range(3, n + 1):
			sum = pre + cur
			pre = cur
			cur = sum
		return sum