class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = []
        for i in range(n):
            players.append(i + 1)

        idx: int = 0
        while len(players) > 1:
            idx += k - 1
            idx %= len(players)
            players.pop(idx)

        return players[0]
