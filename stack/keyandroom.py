# -*- coding: gbk -*-
# ��Ŀ��Դ
# https://leetcode-cn.com/explore/learn/card/queue-stack/220/conclusion/893/

# ����: [[1],[2],[3],[]]
# ���: true
# ����:
# ���Ǵ� 0 �ŷ��俪ʼ���õ�Կ�� 1��
# ֮������ȥ 1 �ŷ��䣬�õ�Կ�� 2��
# Ȼ������ȥ 2 �ŷ��䣬�õ�Կ�� 3��
# �������ȥ�� 3 �ŷ��䡣
# ���������ܹ�����ÿ�����䣬���Ƿ��� true��

class Solution:
	def canVisitAllRooms(self, rooms) -> bool:
		queue = []
