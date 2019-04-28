class BaseClass():
    def __init__(self):
        self.counter = 0

    def add(self, val):
        if val == 1:
            self.add_one() # this causes infinite loop
        else:
            self.counter += val

    def add_one(self):
        self.counter += 1


class SubClass(BaseClass):
    def add_one(self):
        self.add(1)


a = BaseClass()
a.add_one()
print(a.counter)

b = SubClass()
b.add_one()
print(b.counter)