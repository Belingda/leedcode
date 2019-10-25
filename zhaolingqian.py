# -*- coding:utf-8 -*-
# https://leetcode-cn.com/problems/coin-change/solution/dong-tai-gui-hua-tao-lu-xiang-jie-by-wei-lai-bu-ke/
# 322题 零钱兑换

# 说明

class Solution(object):
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





ob = Solution()
print ob.coinChange([3,4,4],1)