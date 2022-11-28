from abc import abstractmethod, ABC


# abstract class
class Product(ABC):
    def __init__(self, name, price, qoh):
        self.name = name
        self.price = price
        self.qoh = qoh

    def purchase(self, qty):
        self.qoh += qty

    def sell(self, qty):
        self.qoh -= qty

    @abstractmethod
    def getsellingprice(self):
        pass


class TaxableProduct(Product):
    def __init__(self, name, price, qoh, taxper):
        super().__init__(name, price, qoh)
        self.taxper = taxper

    def getsellingprice(self):
        return self.price + self.price * self.taxper // 100


class DiscountedProduct(Product):
    def __init__(self, name, price, qoh, disper):
        super().__init__(name, price, qoh)
        self.disper = disper

    def getsellingprice(self):
        return self.price - self.price * self.disper // 100


class ImportedProduct(TaxableProduct):
    def __init__(self, name, price, qoh, taxper, importduty):
        super().__init__(name, price, qoh, taxper)
        self.importduty = importduty

    def getsellingprice(self):
        price1 = self.price + self.price * self.importduty // 100
        return price1 + price1 * self.taxper // 100


p1 = ImportedProduct("iPhone 14 Pro", 100000, 10, 18, 10)
print(p1.getsellingprice())
