# -*- coding: gbk -*-
# 按摩师和打家劫舍1 两道题目其实是一样的 dp思想  dp[i] = max(dp[i-1],dp[i-2]+nums[i])
# https://leetcode-cn.com/problems/the-masseuse-lcci/
# 17.16 按摩师
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
			dp[i] = max(dp[i-1],dp[i-2]+nums[i]) # 取 要么是昨天预约，要么是前天加今天 两者的最大值
		return dp[len(nums)-1]



# https://leetcode-cn.com/problems/house-robber/
# leetcode198 打家劫舍
class Solution2:
	def rob(self, nums) -> int:
		if not nums:
			return 0
		dp0 = 0 # 前天
		dp1 = nums[0] # 昨天
		for i in range(1,len(nums)):
			temp = dp1
			dp1 = max(dp1,dp0+nums[i])
			dp0 = temp
		return dp1

# https://leetcode-cn.com/problems/house-robber-ii/
# 打家劫舍2
class Solution3:
	def rob(self, nums) -> int:
		if len(nums) == 1:
			return nums[0]
		return max(self.robOnce(nums[:-1]),self.robOnce(nums[1:]))

	def robOnce(self,nums):
		if not nums:
			return 0
		dp0 = 0 # 前天
		dp1 = nums[0] # 昨天
		for i in range(1,len(nums)):
			temp = dp1
			dp1 = max(dp1,dp0 + nums[i])
			dp0 = temp
		return dp1

# https://leetcode-cn.com/problems/house-robber-iii
# 打家劫舍3
# max(dp[i-1],dp[i-2]+nums[i])
# 输入: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
# 3 3 1 | 2 3
# 输出: 7
# 解释:小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber-iii

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