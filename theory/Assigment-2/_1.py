# Suppose you have given the stock prices for
# respective days like (100, 180, 260, 310, 40, 535,
# 695). The stock price for the 1st day is 100, 2nd
# day it is 180 and so on. Write a Python program to
# determine what days the user should buy and sell
# the stocks to get the maximum profit. Plot the data
# with day and price.

# stockes = [100, 180, 260, 310, 40, 535,695]

# stockes.sort()
# print(stockes)

# buy = input("Enter the price for buy stockes from this:(100, 180, 260, 310, 40, 535,695)")


import matplotlib.pyplot as plt

def find_buy_sell_days(prices):
    n = len(prices)
    if n == 1:
        return  # No profit can be made if there's only one day of data
    
    buy_sell_pairs = []
    i = 0
    while i < n - 1:
        # Find the local minimum (buying point)
        while (i < n - 1) and (prices[i + 1] <= prices[i]):
            i += 1
        if i == n - 1:
            break
        buy = i
        i += 1
        
        # Find the local maximum (selling point)
        while (i < n) and (prices[i] >= prices[i - 1]):
            i += 1
        sell = i - 1
        
        buy_sell_pairs.append((buy, sell))
        # Print the buy and sell days
        print(f"Buy stock on day {buy + 1} at price {prices[buy]}")
        print(f"Sell stock on day {sell + 1} at price {prices[sell]}")
    
    return buy_sell_pairs

def plot_stock_data(prices, buy_sell_pairs):
    days = list(range(1, len(prices) + 1))
    
    # Plot the prices
    plt.plot(days, prices, marker='o', label='Stock Prices')
    
    # Mark buy and sell points
    for buy, sell in buy_sell_pairs:
        plt.scatter(buy + 1, prices[buy], color='green', label='Buy', marker='^', s=150)
        plt.scatter(sell + 1, prices[sell], color='red', label='Sell', marker='v', s=100)
    
    plt.title('Stock Prices vs Days')
    plt.xlabel('Day')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

# Example usage
prices = [100, 180, 260, 310, 40, 535, 695]
buy_sell_pairs = find_buy_sell_days(prices)

# Plotting the data
plot_stock_data(prices, buy_sell_pairs)
