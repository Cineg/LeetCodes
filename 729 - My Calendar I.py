class MyCalendar:

    def __init__(self) -> None:
        self.bookings: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        if len(self.bookings) == 0 or self._check_collision(start, end):
            self.bookings.append((start, end))
            self.bookings = sorted(self.bookings)
            return True

        return False

    def _check_collision(self, start: int, end: int) -> bool:
        # edge cases
        if self.bookings[0][0] > end:
            return True
        if self.bookings[-1][1] <= start:
            return True

        for booking in self.bookings:
            if booking[0] <= start < booking[1]:
                return False

            if booking[0] < end <= booking[1]:
                return False

            if start <= booking[0] <= booking[1] <= end:
                return False

        return True


def main() -> None:
    obj = MyCalendar()

    for l, r in [
        [97, 100],
        [33, 51],
        [89, 100],
        [83, 100],
        [75, 92],
        [76, 95],
        [19, 30],
        [53, 63],
        [8, 23],
        [18, 37],
        [87, 100],
        [83, 100],
        [54, 67],
        [35, 48],
        [58, 75],
        [70, 89],
        [13, 32],
        [44, 63],
        [51, 62],
        [2, 15],
    ]:
        print(obj.book(l, r))


if __name__ == "__main__":
    main()
