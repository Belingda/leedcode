# -*- coding:utf-8 -*-
import pdb
# 1 ======跳台阶（牛客）
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

# 2 ========斐波切数列（牛客）
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

# 3========322题 零钱兑换
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

	def coinChange2(self, coins, amount):
		if amount == 0:
			return 0
		maxn = pow(2,31)-1
		dp = [[maxn for ci in range(len(coins))] for m in range(amount+1)]
		for m in range(1,amount+1):# money = 0~凑齐的金额总数
			for ci in range(len(coins)):
					if coins[ci] == m:
						dp[m][ci] = 1
					else:
						temp = maxn
						if coins[ci] <m and dp[m - coins[ci]][ci] != maxn:
							temp = dp[m - coins[ci]][ci] + 1
						dp[m][ci] = min(temp,dp[m][ci-1])

		minres = dp[amount][len(coins)-1]
		return -1 if minres > amount else minres


# （4）53题 找出最大连续子序列的和
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
# （5）198题目 找出非连续元素相加的最大值
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
		for i in range(2,len(nums)):
			dp.append(max(dp[i-2]+nums[i],dp[i-1]))
		return dp[len(nums)-1]

# （6）70题目 爬楼梯
class Solution6(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# n=1 f(1)=1
		# n=2 f(2)=2
		# n=3 f(n)=f(n-1)+f(n-2)
		if n == 1:
			return 1
		if n == 2:
			return 2
		dp = [1, 2]
		for i in range(2,n):
			dp.append(dp[i - 1] + dp[i - 2])
		return dp[n - 1]

# （7）======矩阵的最小路径和（左）
def start():
	row,col = map(int,input().split())
	if row <= 0 or col <=0:
		return 0
	m = []
	for i in range(row):
		m.append(list(map(int, input().split())))
	print(GetMinRoute(m,row,col))

def GetMinRoute(m, row, col):
	dp = [[0 for i in range(col)] for i in range(row)]
	dp[0][0] = m[0][0]
	for i in range(1, row):
		dp[i][0] = dp[i - 1][0] + m[i][0]
	for j in range(1, col):
		dp[0][j] = dp[0][j - 1] + m[0][j]

	for i in range(1, row):
		for j in range(1, col):
			dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + m[i][j]
	return dp[row - 1][col - 1]

start()

# （8）=====最长的公共子序列和(左)
class Solution(object):
	def GetLongestSubStrDP(self,s1,s2):
		if len(s1) == 0 or len(s2) == 0:
			return
		dp = [[0 for i in range(len(s2))] for j in range(len(s1))]
		for i in range(len(s1)):
			for j in range(len(s2)):
				if s1[i] == s2[j]:
					if i == 0:
						if j == 0:
							dp[i][j] = 1
						else:
							dp[i][j] = dp[i][j-1] +1

					else:
						dp[i][j] = max(dp[i-1][j],dp[i][j-1])+1
				else:
					if i == 0 :
						if j > 0:
							dp[i][j] = dp[i][j - 1]
					else:
						dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
		return dp[len(s1)-1][len(s2)-1]

	def PrintDP(self,dp):
		for l in dp:
			print("%s\n"%l)

# （9）判断是否为子串（leetcode） #非动态规划解法
class Solution3(object):
	def isSubsequence(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if len(s) == 0:
			return True
		si=0
		for ti in range(len(t)):
			if si >len(s) -1:
				return True
			if t[ti] == s[si]:
				si += 1
		if si<=len(s)-1:
			return False
		return True

# 跳跃游戏（待）


















