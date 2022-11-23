class Course:
    # Constructor
    def __init__(self, title, duration, fee=None):
        # Object Attributes
        self.duration = duration
        self.title = title
        self.__fee = fee  # private attribute
        self.taxper = 12

    # Convert object to str
    def __str__(self):
        return f"{self.title} - {self.duration} - {self.__fee}"

    def getfee(self):
        return self.__fee + (self.__fee * self.taxper / 100)


c1 = Course("Python", 36, 10000)  # Create Object
print(c1.__fee)
