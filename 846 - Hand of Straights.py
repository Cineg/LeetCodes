class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        hand.sort()
        temp: list[int] = hand.copy()

        if len(hand) % groupSize:
            return False

        cards: dict[int, int] = {}
        cards_arr: list[int] = []

        for card in hand:
            if card not in cards_arr:
                cards_arr.append(card)
            if card in cards:
                cards[card] += 1
            else:
                cards[card] = 1

        while temp:
            card: int = temp[0]

            for i in range(groupSize):
                if card + i not in cards or card + i not in temp:
                    return False

                cards[card + i] -= 1
                temp.remove(card + i)

        for card in cards.values():
            if card != 0:
                return False

        return True


def main() -> None:
    sol = Solution()
    hand: list[int] = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize: int = 3

    res: bool = sol.isNStraightHand(hand, groupSize)
    print(res)


if __name__ == "__main__":
    main()
