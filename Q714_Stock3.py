def maxProfit(prices: list[int], fee: int) -> int:
    # Similar to Q309, but there are 2 states at the end of each day
    hold = float("-inf")
    sold = 0

    for p in prices:
        prev_hold, prev_sold = hold, sold

        # To get to hold status, one must buy during the day
        hold = max(prev_hold, prev_sold - p)
        # To get to sold status, one must sell during the day and be charged fee
        sold = max(prev_sold, prev_hold + p - fee)

    return sold


if __name__ == "__main__":
    p1 = [1, 3, 2, 8, 4, 9]
    f1 = 2
    p2 = [1, 3, 7, 5, 10, 3]
    f2 = 3
    print(maxProfit(p1, f1))
    print(maxProfit(p2, f2))
