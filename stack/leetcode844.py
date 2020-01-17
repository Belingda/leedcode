# -*- coding: gbk -*-
'''
���� S �� T �����ַ����������Ƿֱ����뵽�հ׵��ı��༭�����ж϶����Ƿ���ȣ������ؽ���� # �����˸��ַ���

ʾ�� 1��

���룺S = "ab#c", T = "ad#c"
�����true
���ͣ�S �� T ������ ��ac����

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/backspace-string-compare
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������

'''

'''
��ջ
ʱ�临�Ӷȣ�O(M + N)O(M+N)������ M, NM,N ���ַ��� S �� T �ĳ��ȡ�
�ռ临�Ӷȣ�O(M + N)O(M+N)��
'''


class Solution:
	def backspaceCompare(self, S: str, T: str) -> bool:
		self.TempCharStack1 = []
		self.TempCharStack2 = []
		temps =self.DealStr(S)
		tempt =self.DealStr(T)
		return temps == tempt

	def DealStr(self,s):
		tempstack = []
		for c in s:
			if c == "#":
				tempstack.pop() if len(tempstack) > 0 else None
			else:
				tempstack.append(c)
		return tempstack
