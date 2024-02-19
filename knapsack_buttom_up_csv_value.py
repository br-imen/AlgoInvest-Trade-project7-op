
from pandas import read_csv

data = read_csv('data/dataset1_Python+P7.csv')
data = data[data['price'] > 0]
names = data['name'].tolist()
prices_list = data['price'].multiply(100).astype('int').tolist()
profits_list = data['profit'].tolist()
budget = 500*100

print("****End of creating lists ****")


def knapsack(profits, prices, max_weight):
    # Initialize a 2D array with zeros
    dp_table = [[0 for _ in range(max_weight + 1)] for _ in range(len(profits) + 1)]

    # Fill the table with the optimal values for each weight and item combination
    for i in range(1, len(profits) + 1):
        for w in range(1, max_weight + 1):
            if prices[i - 1] > w:
                dp_table[i][w] = dp_table[i -1][w]
            else:
                dp_table[i][w] = max(dp_table[i - 1][w],
                                     (dp_table[i -1][w - prices[i - 1]] + int((profits[i -1] * prices[i - 1]))))
    # Backtrack to find the selected items
    selected_items = []
    price_total = 0
    w = max_weight
    for i in range(len(profits), 0, -1):
        if dp_table[i][w] != dp_table[i - 1][w]:
            selected_items.append(names[i - 1])
            price_total += prices[i - 1]
            w -= prices[i -1]

    # Return the total value and selected items
    return price_total, dp_table[-1][-1], selected_items


def main():
    price_total, total_value, selected_items = knapsack(profits_list, prices_list, budget)

    print("Total price:", price_total/100)
    print("Total value:", total_value/100)
    print("Selected items:", selected_items)


if __name__ == "__main__":
    main()