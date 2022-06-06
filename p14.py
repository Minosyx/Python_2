class Punkt:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Punkt(1, 2)
# p.a = 3
p.x = 5
print(p.x)

print(dir(Punkt))
