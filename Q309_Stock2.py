def maxProfit(prices: list[int]) -> int:
    if not prices:
        return 0
    # 3 states at the end of each day:
    # HOLD: Bought a stock and now holding it (profit -= price)
    # SOLD: Sold a stock that day (profit +- price)
    # REST: Cooldown after yesterday's sold (ready to buy) or just doing nothing (profit unchanged)
    # At the start, hold and sold states are impossible, only rest state is possible with profit of 0.
    hold = float("-inf")
    sold = float("-inf")
    rest = 0

    for p in prices:
        prev_hold, prev_sold, prev_rest = hold, sold, rest

        # Newly bought a stock or continue holding a stock bought previously
        hold = max(prev_hold, prev_rest - p)
        # Sold a stock, add the profit. Can only sell if holding a stock yesterday.
        sold = prev_hold + p
        # Resting yesterday or sold yesterday
        rest = max(prev_sold, prev_rest)

        print(f"PREV: {prev_hold}, {prev_sold}, {prev_rest}\nCURR with {p}: {hold}, {sold}, {rest}")

    
    return max(sold, rest)

if __name__ == "__main__":
    p1 = [7, 1, 5, 3, 6, 4]
    p2 = [7, 6, 4, 3, 1]
    p3 = [2, 4, 1]
    print(maxProfit(p1))
    print(maxProfit(p2))
    print(maxProfit(p3))