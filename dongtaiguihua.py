# -*- coding:utf-8 -*-
import pdb
# ======跳台阶（牛客）
class Solution:
	def jumpFloor(self, number):
		if number <= 0:
			return 0
		if number == 1:
			return 1
		if number == 2:
			return 2
		res = [1, 2]
		for i in range(2, number):
			res.append(res[i - 1] + res[i - 2])
		return res[number - 1]

	def jumpFloor2(self, number):
		if number <= 0:
			return 0
		if number == 1:
			return 1
		if number == 2:
			return 2
		pre = 1
		cur = 2
		sum = pre + cur
		for i in range(3, number + 1):
			sum = pre + cur
			pre = cur
			cur = sum
		return sum

# ========斐波切数列（牛客）
class Solution2:
	def Fibonacci(self, n):
		if n <= 0:
			return 0
		if n == 1:
			return 1
		if n == 2:
			return 1
		pre = 1
		cur = 1
		sum = pre + cur
		for i in range(3, n + 1):
			sum = pre + cur
			pre = cur
			cur = sum
		return sum

# ========322题 零钱兑换
# https://leetcode-cn.com/problems/coin-change/solution/dong-tai-gui-hua-tao-lu-xiang-jie-by-wei-lai-bu-ke/
class Solution3(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		dp = [0]
		maxint = pow(2, 31) - 1 # 这里默认取整数的最大值用于表示默认没有方法可以凑齐硬币
		for i in xrange(1, amount + 1):
			dp.append(maxint)
		for a in xrange(1,amount+1):
			for coin in coins:
				if coin <= a:
					dp[a] = min(dp[a],dp[a-coin] + 1)
		return -1 if dp[amount] > amount else dp[amount] # 如果超了说明没有方法

# 53题 找出最大连续子序列的和
# https://leetcode-cn.com/problems/maximum-subarray/
class Solution4(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			return 0
		sum = nums[0]
		maxn = nums[0]
		for curi in xrange(1, len(nums)):
			if sum + nums[curi] > nums[curi]:
				sum = sum + nums[curi] # 如果sum小于当前数
				maxn = max(maxn, sum)
			else:
				sum = nums[curi]
				maxn = max(maxn, sum)
		return maxn

ob = Solution4()
print [-2,-1]
print ob.maxSubArray([-2,-1])

#[2,1,1,2]
# 198题目 找出非连续元素相加的最大值
# https://leetcode-cn.com/problems/house-robber
class Solution5(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			return 0
		if len(nums) == 1:
			return nums[0]
		dp=[nums[0],max(nums[0],nums[1])]
		for i in xrange(2,len(nums)):
			dp.append(max(dp[i-2]+nums[i],dp[i-1]))
		return dp[len(nums)-1]


