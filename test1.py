# 最长的公共子序列和(左)
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

# ob = Solution()
# print(ob.GetLongestSubStrDP('1A2C3D4B56','B1D23CA45B6A'))

# 零钱兑换
class Solution2(object):
	def coinChange(self, coins, amount):
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

	# def printView(self,dp):
	# 	for d in dp:
	# 		print("%s\n"%d)

# 判断是否为子串（leetcode）
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

ob=Solution3()
s = "acb"
t = "ahbgdc"
print(ob.isSubsequence(s,t))



