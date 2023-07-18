from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_minimum_position = 0
        sell_maximum_position = 1
        max_profit = 0

        while sell_maximum_position < len(prices):
            current_profit = prices[sell_maximum_position] - prices[buy_minimum_position]
    
            if prices[buy_minimum_position] > prices[sell_maximum_position]:
                buy_minimum_position = sell_maximum_position
            else:
                max_profit = max(current_profit, max_profit)
            
            sell_maximum_position += 1

        return max_profit

def main():
    solution = Solution()

    prices = [7,1,5,3,6,4]
    solution.maxProfit(prices)
    
if __name__ == "__main__":
    main()