class LRUCache:
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
            return self.cache[key]
        return -1

    def set(self, key, value):
        if key not in self.cache and len(self.cache) == self.capacity:
            self.cache.popitem(last = False)
        elif key in self.cache:
            del self.cache[key]
        self.cache[key] = value