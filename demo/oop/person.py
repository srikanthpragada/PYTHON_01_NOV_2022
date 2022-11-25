class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}  - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    @property
    def category(self):
        if self.age < 30:
            return "Young"
        elif self.age < 60:
            return "Middle aged"
        else:
            return "Old"


p1 = Person("Andy", 30)
print(p1.category)

p2 = Person("Jason", 40)
p3 = Person("Andy", 30)
print(p1 == p3)  # p1.__eq__(p3)

print(str(p1))  # p1.__str__()

print(p2 > p1)  # p2.__gt__(p1)

l = [p1, p2, p3]

for p in sorted(l):
    print(p)
