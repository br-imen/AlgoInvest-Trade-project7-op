from itertools import combinations
from pandas import read_csv
import time

data = read_csv('data/dataset1_Python+P7.csv')
data = data[data['price'] > 0].to_dict(orient='records')
MAX_COST = 100

# data = [{"name":'Action-1', 'cost': 20, "benefits":0.05},
#         {"name":'Action-2', 'cost': 30, "benefits":0.1},
#         {"name":'Action-3', 'cost':50, "benefits": 0.15},
#         {"name":'Action-4', 'cost':40, "benefits": 0.20},        
#         {"name":'Action-6', 'cost':30, "benefits":0.25},
#         {"name":'Action-7', 'cost':20, "benefits":0.25},
#         {"name":'Action-8', 'cost':22, "benefits":0.07}]


if __name__ == "__main__":
    start_time = time.time()
    combs = []
    for i in range(len(data)):
        combs += list(combinations(data, i+1))
    max_profit = 0
    best_comb = None
    for comb in combs:
        cost = sum((x['cost'] for x in comb))
        if cost > MAX_COST:
            continue
        profit = sum((x['benefits'] * x['cost'] for x in comb))
        if profit > max_profit:
            max_profit = profit
            best_comb = comb
    end_time = time.time() - start_time

    print("max profit:",max_profit)
    print("Combination: ", best_comb)
    print("Duration:", end_time)
