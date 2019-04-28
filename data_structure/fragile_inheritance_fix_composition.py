class BaseClass():
    def __init__(self):
        self.counter = 0

    def add(self, val):
        if val == 1:
            self.add_one()
        else:
            self.counter += val

    def add_one(self):
        self.counter += 1


class SubClass():
    def __init__(self):
        self.base_class = BaseClass()

    def get_counter(self):
        return self.base_class.counter

    def add(self, val):
        self.base_class.add(val)

    def add_one(self):
        self.base_class.add_one()


a = BaseClass()
a.add_one()
print(a.counter)

b = SubClass()
b.add_one()
print(b.get_counter())