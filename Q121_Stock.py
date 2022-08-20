# Question: Given array prices where each element is the price of given stock on i-th day.
# Find the maximum profit that can be achieved. If no profit, return 0.

def maxProfit(prices):
    profit = 0
    min_price = prices[0]
    for price in prices[1:]:
        # Update the minimum price.
        if price < min_price:
            min_price = price
        # Maximize profit.
        else:
            profit = max(profit, price - min_price)
    return profit


def main():
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7, 6, 4, 3, 1]))
    print(maxProfit([2, 4, 1]))


if __name__ == '__main__':
    main()
    