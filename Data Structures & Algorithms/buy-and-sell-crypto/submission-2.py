class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        bp = 0 
        sp = 1
        while sp < len(prices):            
            if prices[bp] < prices[sp]:
                rp = prices[sp] - prices[bp]
                mp = max(rp, mp)
            else:
                bp = sp
            sp += 1 
        return mp



            
            