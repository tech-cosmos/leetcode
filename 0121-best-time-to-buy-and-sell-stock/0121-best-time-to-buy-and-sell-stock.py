class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        bp=prices[0]
        for price in prices:
            if price>bp:
                if profit<price-bp:
                    profit=price-bp
                    print("Reading profit",profit)
            else:
                bp=price
                print("Updating Base Price", bp)
        return profit