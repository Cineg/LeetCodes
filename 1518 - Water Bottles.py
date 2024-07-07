class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total: int = numBottles

        while numBottles >= numExchange:
            total += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange

        return total
