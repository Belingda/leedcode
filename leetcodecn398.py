# -*- coding: gbk -*-
# ר�� ��ˮ���㷨
"""
����һ�����ܺ����ظ�Ԫ�ص��������飬Ҫ�����������������ֵ������� �����Լ������������һ�������������С�

ע�⣺
�����С���ܷǳ��� ʹ��̫�����ռ�Ľ������������ͨ�����ԡ�

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/random-pick-index
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������
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
