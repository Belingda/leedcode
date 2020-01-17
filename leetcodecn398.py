# -*- coding: gbk -*-
# 专题 蓄水池算法
"""
给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/random-pick-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random
class Solution398(object):

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums
	def pick(self, target):
		"""
		:type target: int
		:rtype: int
		"""
		cnt = 0
		for i,num in enumerate(self.nums):
			if num == target:
				cnt +=1
		resi = random.randint(0,cnt-1)
		return self.nums[resi]
