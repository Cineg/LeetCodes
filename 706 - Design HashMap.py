class MyHashMap:

    def __init__(self):
        self.keys: list = []
        self.values: list = []

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            index: int = self.keys.index(key)
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        if key in self.keys:
            index: int = self.keys.index(key)
            return self.values[index]
        else: return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            index: int = self.keys.index(key)
            self.keys.pop(index)
            self.values.pop(index)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

def main():
    obj = MyHashMap()
    obj.put(1,2)
    print(obj.get(1))
    obj.put(1,3)
    obj.remove(1)
    print(obj.get(1))
    obj.put(1,5)
    print(obj.get(1))

if __name__ == "__main__":
    main()