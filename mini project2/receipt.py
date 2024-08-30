import datetime

class Receipt:
    def __init__(self, tax_rate=0.07):
        self.__tax_rate = tax_rate
        self.__purchases = []

    def receiptToString(self):
        total_cost = sum(item.getPrice() for item in self.__purchases)
        total_tax = sum(item.getTax(self.__tax_rate) for item in self.__purchases)
        grand_total = total_cost + total_tax

        receipt_str = "Receipt"
        receipt_str += f"{'':<20} {datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}\n"

        receipt_str += "-" * 40 + "\n" # 40 dashes
        for item in self.__purchases:
            receipt_str +=item.itemToString() + "\n"
        receipt_str += "-" * 40 + "\n"
        receipt_str += f"{'Sub Total:':<20} {total_cost:.2f}\n"
        receipt_str += f"{'Tax: ':<20} {total_tax:.2f}\n"
        receipt_str += f"{'Total: ':<20} {grand_total:.2f}\n"

        return receipt_str

    def addItem(self, item):
        self.__purchases.append(item)
