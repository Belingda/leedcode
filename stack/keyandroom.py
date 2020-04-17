# -*- coding: gbk -*-
# 题目来源
# https://leetcode-cn.com/explore/learn/card/queue-stack/220/conclusion/893/

# 输入: [[1],[2],[3],[]]
# 输出: true
# 解释:
# 我们从 0 号房间开始，拿到钥匙 1。
# 之后我们去 1 号房间，拿到钥匙 2。
# 然后我们去 2 号房间，拿到钥匙 3。
# 最后我们去了 3 号房间。
# 由于我们能够进入每个房间，我们返回 true。

class Solution:
	def canVisitAllRooms(self, rooms) -> bool:
		queue = []
