class Course:
    # class or static attribute
    taxrate = 12

    @staticmethod  # decorator
    def gettaxrate():
        return Course.taxrate

    # Constructor
    def __init__(self, title, duration, fee=None):
        # Object Attributes
        self.duration = duration
        self.title = title
        self.__fee = fee  # private attribute

    # Convert object to str
    def __str__(self):
        return f"{self.title} - {self.duration} - {self.__fee}"

    def getfee(self):
        return self.__fee + (self.__fee * Course.taxper / 100)


c1 = Course("Python", 36, 10000)  # Create Object
# print(c1.__fee)
print(c1._Course__fee)
print(c1.__dict__)
print(Course.gettaxrate()) # call static method
