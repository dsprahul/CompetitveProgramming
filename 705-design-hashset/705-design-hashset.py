class MyHashSet:

    def __init__(self):
        self.capacity = 10**6 + 1
        self.data = [0] * self.capacity

    def add(self, key: int) -> None:
        self.data[key % self.capacity] = 1
        
    def remove(self, key: int) -> None:
        self.data[key % self.capacity] = 0

    def contains(self, key: int) -> bool:
        return self.data[key % self.capacity] == 1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)