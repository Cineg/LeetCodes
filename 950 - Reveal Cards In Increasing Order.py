from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:

        res = [0] * len(deck)
        q = deque([i for i in range(len(deck))])

        deck.sort()
        deck_q = deque(deck)

        while q:
            first = q.popleft()

            if q:
                second = q.popleft()
                q.append(second)

            res[first] = deck_q.popleft()

        return res


def main():
    sol = Solution()
    sol.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])


if __name__ == "__main__":
    main()
