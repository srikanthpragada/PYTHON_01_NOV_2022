class Course:
    # Constructor
    def __init__(self, title, duration, fee=None):
        # Object Attributes
        self.duration = duration
        self.title = title
        self.fee = fee
        self.taxper = 12

    # Convert object to str
    def __str__(self):
        return f"{self.title} - {self.duration} - {self.fee}"

    # Method
    def show(self):
        print(self.title)
        print(self.duration)
        print(self.fee)

    def getfee(self):
        return self.fee + (self.fee * self.taxper / 100)


c1 = Course("Python", 36, 10000)  # Create Object
# print(c1.fee)
c1.show()
print(c1.getfee())

c2 = Course("Spring Boot", 20)
print(c2)  # c2.__str__()
