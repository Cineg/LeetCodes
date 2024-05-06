class Heap:
    def __init__(self) -> None:
        self.len: int = 0
        self.items: list[int] = []

    def peek(self) -> int | None:
        if self.items:
            return self.items[0]

        return None

    def append(self, val: int) -> None:
        self.items.append(val)
    
        self._bubble_up(self.len)
        self.len += 1

    def pop(self, val: int) -> None:
        idx: int = 0
        while True:
            if self.items[idx] == val:
                break
            idx += 1
        
        self.items[idx], self.items[-1] = self.items[-1], self.items[idx]

        self.items.pop()
        self.len -= 1
        
        self._bubble_down(idx)

    def _bubble_up(self, idx: int) -> None:
        parent_idx: int = (idx - 1) // 2
        if parent_idx < 0:
            return

        if self.items[idx] > self.items[parent_idx]:
            
            self.items[idx], self.items[parent_idx] = (
                self.items[parent_idx],
                self.items[idx],
            )
            
            self._bubble_up(parent_idx)

        return

    def _bubble_down(self, idx: int) -> None:
        ch: int = self._get_child_idx(idx)
        if ch < 0:
            return

        if self.items[ch] < self.items[idx]:
            self.items[ch], self.items[idx] = self.items[idx], self.items[ch]
            self._bubble_down(ch)

        return

    def _get_child_idx(self, idx: int) -> int:
        l: int = idx * 2 + 1
        r: int = idx * 2 + 2

        if l >= self.len:
            return -1
        if r >= self.len:
            return l

        if self.items[l] < self.items[r]:
            return l
        else:
            return r

 

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap = Heap()
        for i in range(k):
            heap.append(nums[i])

        res: list[int] = []
        l: int = 0
        while l + k <= len(nums):
            max_val: int | None = heap.peek()
            if max_val:
                res.append(max_val)

            if l + k == len(nums):
                break

            heap.pop(nums[l])
            heap.append(nums[l + k])
            l += 1

        return res


def main() -> None:
    sol = Solution()
    nums: list[int] = [1,3,-1,-3,5,3,6,7]
    k: int = 3

    res: list[int] = sol.maxSlidingWindow(nums, k)
    print(res)


if __name__ == "__main__":
    main()
