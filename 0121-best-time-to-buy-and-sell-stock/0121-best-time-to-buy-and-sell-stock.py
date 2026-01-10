class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, bp =0, prices[0]
        bp=prices[0]
        for i,price in enumerate(prices):
            if i==0:
                continue
            if price>bp:
                if profit<price-bp:
                    profit=price-bp
            else:
                bp=price
        return profit