class MyDictionary:
    def __init__(self, size: int = 10):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def __setitem__(self, key, value):
        index = hash(key) % self.size
        if self.keys[index] is None or self.keys[index] == key:
            self.keys[index] = key
            self.values[index] = value
        else:
            raise KeyError(f"Коллизия для ключа {key}")

    def __getitem__(self, key):
        index = hash(key) % self.size
        if self.keys[index] == key:
            return self.values[index]
        else:
            raise KeyError(f"Ключ {key} не найден")


dct = MyDictionary(100)
dct["name"] = "Gogi"
print(dct["name"])
print(hash("name") % 100)
