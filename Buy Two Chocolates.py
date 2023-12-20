from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_price1 = float('inf')
        min_price2 = float('inf')

        for price in prices:
            if price < min_price1:
                min_price2 = min_price1
                min_price1 = price
            elif price < min_price2:
                min_price2 = price

        min_sum = min_price1 + min_price2
        return money - min_sum if money - min_sum >= 0 else money
