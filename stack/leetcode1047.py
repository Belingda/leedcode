# -*- coding: gbk -*-

'''
������Сд��ĸ��ɵ��ַ���?S���ظ���ɾ��������ѡ��������������ͬ����ĸ����ɾ�����ǡ�

�� S �Ϸ���ִ���ظ���ɾ��������ֱ���޷�����ɾ����

����������ظ���ɾ�������󷵻����յ��ַ������𰸱�֤Ψһ��

?

ʾ����

���룺"abbaca"
�����"ca"
���ͣ�
���磬�� "abbaca" �У����ǿ���ɾ�� "bb" ��������ĸ��������ͬ�����Ǵ�ʱΨһ����ִ��ɾ���������ظ��֮�����ǵõ��ַ��� "aaca"��������ֻ�� "aa" ����ִ���ظ���ɾ�����������������ַ���Ϊ "ca"��

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������
'''
class Solution:
	def removeDuplicates(self, S: str) -> str:
		tempstack = []
		for c in S:
			if len(tempstack)>0 and c == tempstack[-1]:
				tempstack.pop()
			else:
				tempstack.append(c)
		return ''.join(tempstack)

