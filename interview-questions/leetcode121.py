class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in  range(1,len(prices)):
            max_profit = max(max_profit,prices[i]-min_price)
            min_price = min(min_price,prices[i])
        return max_profit
