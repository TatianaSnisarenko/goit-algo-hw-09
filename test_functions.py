import unittest
from collections import Counter

from functions import find_coins_greedy, find_min_coins_bottom_up, find_min_coins_memo, find_min_coins_lru_cache


class TestFindMinCoins(unittest.TestCase):
    def test_zero_amount(self):
        self.assertEqual(find_min_coins_lru_cache(0), Counter())
        self.assertEqual(find_min_coins_memo(0), Counter())
        self.assertEqual(find_coins_greedy(0), {})
        self.assertEqual(find_min_coins_bottom_up(0), {})

    def test_negative_amount(self):
        self.assertIsNone(find_min_coins_lru_cache(-1))
        self.assertIsNone(find_min_coins_memo(-1))
        self.assertEqual(find_coins_greedy(-1), {})
        self.assertEqual(find_min_coins_bottom_up(-1), {})

    def test_single_coin(self):
        self.assertEqual(find_min_coins_lru_cache(50), Counter({50: 1}))
        self.assertEqual(find_min_coins_memo(50), Counter({50: 1}))
        self.assertEqual(find_coins_greedy(50), {50: 1})
        self.assertEqual(find_min_coins_bottom_up(50), {50: 1})

    def test_multiple_coins(self):
        self.assertEqual(find_min_coins_lru_cache(
            113), Counter({50: 2, 10: 1, 2: 1, 1: 1}))
        self.assertEqual(find_min_coins_memo(
            113), Counter({50: 2, 10: 1, 2: 1, 1: 1}))
        self.assertEqual(find_coins_greedy(113), {50: 2, 10: 1, 2: 1, 1: 1})
        self.assertEqual(find_min_coins_bottom_up(113),
                         {50: 2, 10: 1, 2: 1, 1: 1})

    def test_no_solution(self):
        self.assertIsNone(find_min_coins_lru_cache(3, (5, 10)))
        self.assertIsNone(find_min_coins_memo(3, (5, 10)))
        self.assertEqual(find_coins_greedy(3, (5, 10)), {})
        self.assertEqual(find_min_coins_bottom_up(3, (5, 10)), {})


if __name__ == '__main__':
    unittest.main()
