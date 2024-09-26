
class StopError(ValueError):
    pass

class iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StopError()
        else:
            self.start, self.stop, self.step, self.pioner = start, stop, step, start

    def __iter__(self):
        self.pioner = self.start - self.step
        return self

    def __next__(self):
        self.pioner += self.step
        if (self.pioner > self.stop and self.step > 0) or (self.pioner < self.stop and self.step < 0):
            raise StopIteration()
        return self.pioner

try:
    iter1 = iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StopError:
    print('Шаг указан неверно')

iter2 = iterator(-5, 1)
iter3 = iterator(6, 15, 2)
iter4 = iterator(5, 1, -1)
iter5 = iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')