# -*- coding: gbk -*-
'''
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/backspace-string-compare
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

'''
用栈
时间复杂度：O(M + N)O(M+N)，其中 M, NM,N 是字符串 S 和 T 的长度。
空间复杂度：O(M + N)O(M+N)。
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
