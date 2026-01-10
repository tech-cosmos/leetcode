class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, bp =0, prices[0]
        bp=prices[0]
        for price in prices[1:]:
            if price>bp:
                if profit<price-bp:
                    profit=price-bp
            else:
                bp=price
        return profit