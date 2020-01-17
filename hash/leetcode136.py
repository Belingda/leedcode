# -*- coding: gbk -*-
'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 思路一
'''
不使用额外空间 异或算法 相同数异或为0
'''

class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		sum = 0
		for i in nums:
			sum = sum ^ i
		return sum

'''
'''
class Solution2(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		sum = 0

		for i in nums:
			sum = sum ^ i
		return sum
