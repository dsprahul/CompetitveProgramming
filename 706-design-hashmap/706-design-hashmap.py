class MyHashMap:

    def __init__(self):
        self.buckets = 1000
        self.b_cap = 1000
        self.map = [-1] * self.buckets
        self.max_num = False
        
    def _bloc(self, key):
        return key % self.buckets
    
    def _bindex(self, key):
        return key // self.b_cap

    def put(self, key: int, value: int) -> None:
        if key == 10**6:
            self.max_num = value
        else:
            bloc = self._bloc(key)
            if self.map[bloc] == -1:
                self.map[bloc] = [-1] * self.b_cap
            self.map[bloc][self._bindex(key)] = (key, value)


    def get(self, key: int) -> int:
        if key == 10**6:
            return self.max_num
        
        bloc, binx = self._bloc(key), self._bindex(key)
        if self.map[bloc] != -1:
            data = self.map[bloc][binx] 
            if data != -1:
                return data[1]
        
        return -1

    def remove(self, key: int) -> None:
        if key == 10**6:
            self.max_num = False
        
        else:
            bloc, binx = self._bloc(key), self._bindex(key)
            if self.map[bloc] != -1:
                if self.map[bloc][binx] != -1:
                    if self.map[bloc][binx][0] == key:
                        self.map[bloc][binx] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)