
# 买卖股票的最高收益
# 法一：贪心算法：如果后一天的价格比前一天高 那么买进计算收益
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        profit=0
        for i in range(0,len(prices)-1):
            if prices[i+1]>prices[i]:
                profit+=prices[i+1]-prices[i]
        return profit
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        temp=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>temp:
                profit+=prices[i]-temp
            temp=prices[i]
        return profit