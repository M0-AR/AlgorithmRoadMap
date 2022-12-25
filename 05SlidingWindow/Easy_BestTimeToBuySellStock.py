def maximum_profit(prices):
    l, r = 0, 1  # Left=buy, right=sell
    maxProfit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r
        r += 1

    return maxProfit


print(maximum_profit([7, 1, 5, 3, 6, 4]))  # Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                                           # Not 7-1 = 6, we can not come back in time

