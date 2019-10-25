# -*- coding:utf-8 -*-

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
class Solution:
	def VerifySquenceOfBST(self, sequence):
		# write code here
		if sequence is None or len(sequence) == 0:
			return False
		return self.VerifyBST(sequence)

	def VerifyBST(self,verifys):
		if len(verifys) <= 1:  # 只剩根结点
			return True
		root = verifys[-1]
		temps = verifys[:-1]
		lefts = []
		rights = []
		for i in range(len(temps)):
			if temps[i] > root:
				lefts = temps[0:i]
				if i <= len(temps) - 1:
					rights = temps[i:-1]
				break
		else:
			lefts = temps

		for v in lefts:
			if v > root:
				return False

		for v in rights:
			if v < root:
				return False
		return self.VerifyBST(lefts) and self.VerifyBST(rights)

'''
网上看到的不用递归的C++写法 
大致思路是根据后序遍历(左右根），将当前结点作为根结点 遍历结点前面序列的值，如果当前元素值小于结点值
并且前一元素值也大于序列值 说明不是二叉搜索树

'''
# lst= [4,8,6,12,16,14,10]
# ob = Solution()
# print(ob.VerifySquenceOfBST(lst))
# #[4,8,6,12,16,14,10]
#
# if(sequence.length == 0) return false;
# for(int i = 0; i < sequence.length; i++){
# boolean sign = false;
# for(int j = 0; j < i; j++){
# if(sequence[j] > sequence[i]){
# sign = true;
# }
# else if(sign) return false;
# }
# }
# return true;