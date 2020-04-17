# -*- coding: gbk -*-
# ��Ħʦ�ʹ�ҽ���1 ������Ŀ��ʵ��һ���� dp˼��  dp[i] = max(dp[i-1],dp[i-2]+nums[i])
# https://leetcode-cn.com/problems/the-masseuse-lcci/
# 17.16 ��Ħʦ
class Solution:
	def massage(self, nums) -> int:
		if not nums:
			return 0
		if len(nums) == 1:
			return nums[0]
		dp = [0]*len(nums)
		dp[0] = nums[0]
		dp[1] = max(nums[0],nums[1])
		for i in range(2,len(nums)):
			dp[i] = max(dp[i-1],dp[i-2]+nums[i]) # ȡ Ҫô������ԤԼ��Ҫô��ǰ��ӽ��� ���ߵ����ֵ
		return dp[len(nums)-1]



# https://leetcode-cn.com/problems/house-robber/
# leetcode198 ��ҽ���
class Solution2:
	def rob(self, nums) -> int:
		if not nums:
			return 0
		dp0 = 0 # ǰ��
		dp1 = nums[0] # ����
		for i in range(1,len(nums)):
			temp = dp1
			dp1 = max(dp1,dp0+nums[i])
			dp0 = temp
		return dp1

# https://leetcode-cn.com/problems/house-robber-ii/
# ��ҽ���2
class Solution3:
	def rob(self, nums) -> int:
		if len(nums) == 1:
			return nums[0]
		return max(self.robOnce(nums[:-1]),self.robOnce(nums[1:]))

	def robOnce(self,nums):
		if not nums:
			return 0
		dp0 = 0 # ǰ��
		dp1 = nums[0] # ����
		for i in range(1,len(nums)):
			temp = dp1
			dp1 = max(dp1,dp0 + nums[i])
			dp0 = temp
		return dp1

# https://leetcode-cn.com/problems/house-robber-iii
# ��ҽ���3
# max(dp[i-1],dp[i-2]+nums[i])
# ����: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
# 3 3 1 | 2 3
# ���: 7
# ����:С͵һ���ܹ���ȡ����߽�� = 3 + 3 + 1 = 7
# ��Դ�����ۣ�LeetCode��
# ���ӣ�https://leetcode-cn.com/problems/house-robber-iii

# 3 2 3 3 1
# [2, 1, 3, null, 4]
# 2
#1 3
# 4

# 2 1 3 4
# Definition for a binary tree node.
# dp1 = max(dp1,dp0+nums[i])
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution4:
	def rob(self, root: TreeNode) -> int:
		if not root:
			return 0
		queue = [root]
		dp0 = 0
		dp1 = root.val
		while(queue):
			node = queue.pop()
			dp1 = max(dp1,dp0)