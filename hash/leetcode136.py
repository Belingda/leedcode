# -*- coding: gbk -*-
'''
����һ���ǿ��������飬����ĳ��Ԫ��ֻ����һ�����⣬����ÿ��Ԫ�ؾ��������Ρ��ҳ��Ǹ�ֻ������һ�ε�Ԫ�ء�

˵����

����㷨Ӧ�þ�������ʱ�临�Ӷȡ� ����Բ�ʹ�ö���ռ���ʵ����

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/single-number
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������
'''
# ˼·һ
'''
��ʹ�ö���ռ� ����㷨 ��ͬ�����Ϊ0
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
