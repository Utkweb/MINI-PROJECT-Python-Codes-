from item import Item
from receipt import Receipt

def main():
    receipt = Receipt()

    print("Welcome to the Receipt Generator!")
    while True:
        item_name = input("Enter item name (or 'q' to finish): ")
        if item_name.lower() == 'q':
            break

        item_price = float(input("Enter item price: "))
        item_taxable = input("Is the item taxable? (y/n): ").lower() == 'y'

        item = Item(item_name, item_price, item_taxable)
        receipt.addItem(item)

    print("\n" + receipt.receiptToString())

if __name__ == '__main__':
    main()