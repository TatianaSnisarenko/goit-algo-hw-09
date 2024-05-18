import random
import timeit
from collections import Counter
from functools import lru_cache
from collections import defaultdict


def find_coins_greedy(amount, coins=(50, 25, 10, 5, 2, 1)):
    if amount <= 0:
        return {}
    result = defaultdict(int)
    for coin in coins:
        while amount >= coin:
            result[coin] += 1
            amount -= coin
    return dict(result)


def find_min_coins_bottom_up(amount, coins=(50, 25, 10, 5, 2, 1)):
    if amount <= 0:
        return {}
    table = [0] + [float("inf")] * amount
    chosen_coins = [0] + [0] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            if table[i - coin] + 1 < table[i]:
                table[i] = table[i - coin] + 1
                chosen_coins[i] = coin
    if table[amount] == float("inf"):
        return {}
    result = {}
    while amount > 0:
        if chosen_coins[amount] in result:
            result[chosen_coins[amount]] += 1
        else:
            result[chosen_coins[amount]] = 1
        amount -= chosen_coins[amount]
    return result


def find_min_coins_memo(amount, coins=(50, 25, 10, 5, 2, 1), memo=None):
    if memo is None:
        memo = {}
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return Counter()
    if amount < 0:
        return None
    shortest_combination = None
    for coin in coins:
        remainder = amount - coin
        remainder_combination = find_min_coins_memo(remainder, coins, memo)
        if remainder_combination is not None:
            combination = remainder_combination + Counter({coin: 1})
            if shortest_combination is None or len(list(combination.elements())) < len(list(shortest_combination.elements())):
                shortest_combination = combination
    memo[amount] = shortest_combination
    return shortest_combination


@lru_cache(maxsize=None)
def find_min_coins_lru_cache(amount, coins=(50, 25, 10, 5, 2, 1)):
    if amount == 0:
        return Counter()
    if amount < 0:
        return None
    shortest_combination = None
    for coin in coins:
        remainder = amount - coin
        remainder_combination = find_min_coins_lru_cache(remainder, coins)
        if remainder_combination is not None:
            combination = remainder_combination + Counter({coin: 1})
            if shortest_combination is None or len(list(combination.elements())) < len(list(shortest_combination.elements())):
                shortest_combination = combination
    return shortest_combination


if __name__ == "__main__":
    amount = 113

    print(find_coins_greedy(amount))
    print(find_min_coins_bottom_up(amount))
    print(find_min_coins_lru_cache(amount))
    print(find_min_coins_memo(amount))
