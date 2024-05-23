from math import inf


class MinHeap:
    def __init__(self, length: int, nums: list[int]) -> None:
        self.data: list[int] = []
        self.capacity: int = length
        self.len: int = 0
        self.min_val: int | float = -inf

        self._add_nums(nums)

    def add(self, val: int) -> int:
        if val < self.min_val:
            return self.data[0]

        self.data.append(val)
        self.len += 1

        if self.len <= self.capacity:
            self._bubble_up(self._get_parent(self.len - 1), self.len - 1)

        if self.len > self.capacity:
            self.data[0], self.data[-1] = self.data[-1], self.data[0]

            self.data.pop()
            self.len -= 1
            self._bubble_down(0)

        if self.len == self.capacity:
            self.min_val = self.data[0]

        return self.data[0]

    def _get_parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def _swap_parent(self, parent: int, idx: int) -> bool:
        if self.data[parent] > self.data[idx]:
            self.data[parent], self.data[idx] = self.data[idx], self.data[parent]
            return True
        return False

    def _get_children(self, idx: int) -> int:
        c1: int = idx * 2 + 1
        c2: int = idx * 2 + 2

        if c1 > self.len - 1:
            return -1

        if c2 > self.len - 1:
            return c1

        if self.data[c1] <= self.data[c2]:
            return c1
        else:
            return c2

    def _bubble_up(self, parent: int, idx: int) -> None:
        while parent >= 0:
            if not self._swap_parent(parent, idx):
                break

            idx = parent
            parent = self._get_parent(idx)

    def _bubble_down(self, idx: int) -> None:
        child: int = self._get_children(idx)

        if child == -1:
            return

        if not self._swap_parent(idx, child):
            return

        self._bubble_down(child)

    def _add_nums(self, nums: list[int]) -> None:
        for num in nums:
            self.add(num)


class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        self.heap = MinHeap(k, nums)

    def add(self, val: int) -> int:
        return self.heap.add(val)


def main() -> None:
    sol = KthLargest(2, [0])
    print(sol.add(-1))
    print(sol.add(1))
    print(sol.add(-2))
    print(sol.add(-4))
    print(sol.add(3))


if __name__ == "__main__":
    main()

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
