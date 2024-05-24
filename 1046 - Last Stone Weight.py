class MaxHeap:
    def __init__(self) -> None:
        self.len: int = 0
        self.data: list[int] = []

    def add(self, val: int) -> None:
        self.len += 1
        self.data.append(val)
        self._heapify_up(self.len - 1)

    def pop(self) -> int | None:
        if self.len == 0:
            return None

        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        ret: int = self.data[-1]

        self.len -= 1
        self.data.pop()

        self._heapify_down(0)
        return ret

    def _heapify_up(self, idx: int) -> None:
        parent_idx: int = self._get_parent_idx(idx)
        if parent_idx < 0:
            return

        if self.data[idx] > self.data[parent_idx]:
            self.data[idx], self.data[parent_idx] = (
                self.data[parent_idx],
                self.data[idx],
            )
        else:
            return

        self._heapify_up(parent_idx)

    def _heapify_down(self, idx: int) -> None:
        child_idx: int = self._get_child_idx(idx)
        if child_idx == -1:
            return

        if self.data[idx] < self.data[child_idx]:
            self.data[idx], self.data[child_idx] = self.data[child_idx], self.data[idx]
        else:
            return

        self._heapify_down(child_idx)

    def _get_parent_idx(self, idx: int) -> int:
        return (idx - 1) // 2

    def _get_child_idx(self, idx: int) -> int:
        c1: int = (idx * 2) + 1
        c2: int = (idx * 2) + 2

        if c1 > self.len - 1:
            return -1
        if c2 > self.len - 1:
            return c1

        if self.data[c1] > self.data[c2]:
            return c1

        return c2


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = MaxHeap()

        for stone in stones:
            heap.add(stone)

        while heap.len > 1:
            s1: int | None = heap.pop()
            s2: int | None = heap.pop()

            if s1 == None or s2 == None:
                break

            res: int = s1 - s2
            if res != 0:
                heap.add(res)

        result: int | None = heap.pop()

        return result if result != None else 0


def main() -> None:
    sol = Solution()
    stones: list[int] = [10, 4, 2, 10]
    res: int = sol.lastStoneWeight(stones)
    print(res)


if __name__ == "__main__":
    main()
