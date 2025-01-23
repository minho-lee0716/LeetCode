class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        bought_price = prices[0]

        for today_price in prices[1:]:
            if bought_price > today_price:
                bought_price = today_price
            
            mp = max(mp, today_price - bought_price)
        
        return mp