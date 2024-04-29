class TimeMap:
    def __init__(self) -> None:
        self.data: dict[str, dict] = {}
        self.timestamps: dict[str, list] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = {timestamp: value}
            self.timestamps[key] = [timestamp]
            return

        self.data[key][timestamp] = value
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        if timestamp not in self.data[key]:
            closest: int = self._get_closest(key, timestamp)
            return self.data[key][closest] if closest != -1 else ""

        return self.data[key][timestamp]

    def _get_closest(self, key: str, timestamp: int) -> int:
        arr = self.timestamps[key]

        l: int = 0
        r: int = len(arr) - 1

        if arr[l] > timestamp:
            return -1

        if arr[r] < timestamp:
            return arr[r]

        while l < r:
            mid: int = l + (r - l) // 2

            if arr[r] < timestamp:
                return arr[r]

            if timestamp > arr[mid]:
                l = mid + 1
                continue

            if timestamp < arr[mid]:
                r = mid
                continue

        return arr[r] if arr[r] < timestamp else arr[r - 1]


def main() -> None:
    map = TimeMap()
    map.set("assem", "fat", 20)
    map.set("assem", "thin", 40)
    map.set("hamza", "thin", 41)
    print(map.get("hamza", 20))


if __name__ == "__main__":
    main()
