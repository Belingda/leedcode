# -*- coding: gbk -*-
from typing import List
'''
�������ǰ��������¼Ա��
����һ���ַ����б�ÿ���ַ���������������������֮һ��
1.������һ�ֵĵ÷֣���ֱ�ӱ�ʾ���ڱ����л�õĻ�������
2. "+"��һ�ֵĵ÷֣�����ʾ���ֻ�õĵ÷���ǰ������Ч?�غϵ÷ֵ��ܺ͡�
3. "D"��һ�ֵĵ÷֣�����ʾ���ֻ�õĵ÷���ǰһ����Ч?�غϵ÷ֵ�������
4. "C"��һ���������ⲻ��һ���غϵķ���������ʾ����õ����һ����Ч?�غϵķ�������Ч�ģ�Ӧ�ñ��Ƴ���

ÿһ�ֵĲ������������Եģ����ܻ��ǰһ�ֺͺ�һ�ֲ���Ӱ�졣
����Ҫ�����������лغ��е÷ֵ��ܺ͡�

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/baseball-game
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������
'''

'''
�ҵ���� ����ջ����ÿһ�ֽ�� ���ɽ�� 
'''


# ["5","2","C","D","+"]
class Solution:
	def calPoints(self, ops: List[str]) -> int:
		self.Ops = ops
		self.TempOpsStack = []
		sum = 0
		for symbol in ops:
			if symbol == 'C':
				sum -= self.PopLastScore()
			elif symbol == 'D':
				sum += self.GetDoubleScore()
			elif symbol == '+':
				sum += self.GetBeforeTwoScore()
			else:
				sum += int(symbol)
				self.TempOpsStack.append(int(symbol))
		return sum

	def PopLastScore(self):
		return self.TempOpsStack.pop()

	def GetDoubleScore(self):
		score = self.TempOpsStack[-1]*2
		self.TempOpsStack.append(score)
		return score

	def GetBeforeTwoScore(self):
		addscore = self.TempOpsStack[-1] + self.TempOpsStack[-2]
		self.TempOpsStack.append(addscore)
		return addscore
