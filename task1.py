import random
import timeit
from collections import Counter
from functools import lru_cache
from collections import defaultdict
from functions import find_coins_greedy, find_min_coins_bottom_up, find_min_coins_memo, find_min_coins_lru_cache
import pandas as pd


def average_time(amounts, coin_funcs):
    results = []
    for coin_func in coin_funcs:
        total_time = 0
        for amount in amounts:
            start_time = timeit.default_timer()
            coin_func(amount)
            end_time = timeit.default_timer()
            total_time += end_time - start_time
        avg_time = round(total_time / len(amounts) * 1000, 6)
        results.append({
            'function': coin_func.__name__,
            'average_time': avg_time
        })
    return pd.DataFrame(results)


if __name__ == "__main__":

    functions = [find_coins_greedy,
                 find_min_coins_lru_cache,
                 find_min_coins_bottom_up,
                 find_min_coins_memo]

    print("Середні часи виконання функцій для 10000 випадкових сум з amount у межах 100:")
    amounts = random.choices(range(1, 101), k=10000)

    print(average_time(amounts, functions).to_string(index=False))

    print("Середні часи виконання функцій для 100 випадкових великих сум з amount у межах 1000-1100:")
    amounts = random.choices(range(1000, 1101), k=100)
    print(average_time(amounts, functions).to_string(index=False))

    print("Середні часи виконання функцій для 10000 випадкових великих сум з amount у межах 1000-1100:")
    amounts = random.choices(range(1000, 1101), k=10000)
    print(average_time(amounts, functions[:-1]).to_string(index=False))
