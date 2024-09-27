class MyCalendar:

    def __init__(self) -> None:
        self.bookings: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        for left, right in self.bookings:
            if start < right and end > left:
                overlap: tuple[int, int] = (max(left, start), min(right, end))
                if not self._can_book(overlap[0], overlap[1]):
                    return False

            self.bookings.append((start, end))
            return True

    def _can_book(self, start: int, end: int, max_overlaps: int = 2) -> bool:
        overlaps: int = 0
        for left, right in self.bookings:
            if start < right and end > left:
                overlaps += 1

            if overlaps == max_overlaps:
                return False

        return True


def main() -> None:
    obj = MyCalendar()

    for l, r in [
        [5, 12],
        [42, 50],
        [4, 9],
        [33, 41],
        [2, 7],
        [16, 25],
        [7, 16],
        [6, 11],
        [13, 18],
        [38, 43],
        [49, 50],
        [6, 15],
        [5, 13],
        [35, 42],
        [19, 24],
        [46, 50],
        [39, 44],
        [28, 36],
        [28, 37],
        [20, 29],
        [41, 49],
        [11, 19],
        [41, 46],
        [28, 37],
        [17, 23],
        [22, 31],
        [4, 10],
        [31, 40],
        [4, 12],
        [19, 26],
    ]:
        if l == 41:
            print("hehehe")
        print(obj.book(l, r))


if __name__ == "__main__":
    main()
