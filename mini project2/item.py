class Item:
    def __init__(self, name, price, taxable):
        self.__name = name
        self.__price = price
        self.__taxable = taxable

    def itemToString(self):
        return f"{self.__name:<20} {self.__price:.2f}"

    def getPrice(self):
        return self.__price

    def getTax(self, tax_rate):
        if self.__taxable:
            return self.__price * tax_rate
        else:
            return 0.0