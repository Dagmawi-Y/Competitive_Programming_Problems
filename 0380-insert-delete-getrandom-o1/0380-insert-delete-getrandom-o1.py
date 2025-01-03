class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        if val not in self.num_map:
            self.num_map[val] = len(self.num_list)
            self.num_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.num_map:
            index = self.num_map[val]
            last_val = self.num_list[-1]
            self.num_list[index] = last_val
            self.num_map[last_val] = index
            self.num_list.pop()
            del self.num_map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.num_list)