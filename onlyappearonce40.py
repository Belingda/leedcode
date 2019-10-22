# -*- coding:utf-8 -*-


# 要求时间复杂度o(n) 空间复杂度o(1)
class Solution:
	# 返回[a,b] 其中ab是出现一次的两个数字
	def FindNumsAppearOnce(self, array):
		if array is None or len(array) == 0:
			return []
		res = 0
		for a in array:
			res = res ^ a # 将所有数异或，相同的数异或后为0，异或结果中位数中出现的1为A和B不相同的位数
		if res == 0:
			return []

		temp = res
		bit = 0 # 从右边数起第N位
		while (temp & 1 == 0):# 查找二进制下从右边数起的第1个为1的位数
			temp = temp >> 1
			bit += 1
		a1 = []
		a2 = []
		for a in array:
			res2 = a >> bit & 1 # 查看第N位是1还是0
			if res2 == 1:
				a1.append(a)
			if res2 == 0:
				a2.append(a)
		arrayres = []
		res3 = 0
		res4 = 0
		for a in a1:
			res3 = res3 ^ a
		arrayres.append(res3)
		for a in a2:
			res4 = res4 ^ a
		arrayres.append(res4)
		return  arrayres
'''
异或：相同的数异或后为0
与运算：n和1进行与运算 最低位为1是结果为1 为0是结果为0
'''