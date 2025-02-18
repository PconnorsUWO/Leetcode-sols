from typing import List
def maxProfit(prices: List[int]) -> int:
    buy_price = prices[0]
    profit = -1
    for i in prices:
        if i < buy_price:
            buy_price = i
        profit = max(i - buy_price, profit)

    return profit