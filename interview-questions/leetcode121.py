def maxProfit(self, prices):
      """
      :type prices: List[int]
      :rtype: int
      """
      max_profit = 0
      for i in range(len(prices)):
          cur_profit = -prices[i]
          for j in range(i,len(prices)):
              max_profit = max(max_profit,cur_profit+prices[j])
      return max_profit
