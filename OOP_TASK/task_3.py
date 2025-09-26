class Item:
    def __init__(self, name, price, quantity=1):
        
        if not isinstance(name, str) or not name.strip():
            print("Item name must be a non-empty string.")
            return

        if not isinstance(price, (int, float)) or price <= 0:
            print("Item price must be a positive number.")
            return

        if not isinstance(quantity, int) or quantity < 0:
            print("Quantity must be a non-negative integer.")
            return

        self.name = name.strip()
        self.price = float(price)
        self.quantity = quantity

    # def __str__(self):
    #     return f"{self.name} - ${self.price:.2f} (Stock: {self.quantity})"


class VendingMachine:
    def __init__(self):
        self.items = []
        self.sold = 0
        self.revenue = 0.0

    def add_item(self, item):
        for current_item in self.items:
            if current_item.name.lower() == item.name.lower() and current_item.price == item.price:
                current_item.quantity += item.quantity
                return
        self.items.append(item)

    def add_bulk_items(self, items):
        for item in items:
            self.add_item(item)

    def show_items(self):
        if not self.items:
            print("No items available.")
            return
        
        print("Items available:")
        for i, item in enumerate(self.items, start=1):
            # print(f"{i}. {item}")
            print(f"{i}. {item.name} - ${item.price:.2f} (Stock: {item.quantity})")

    def show_stats(self):
        print(f"Total items sold: {self.sold}")
        print(f"Total revenue: ${self.revenue:.2f}")

    def buy_item(self, item_number, money):
        if not isinstance(money, (int, float)) or money <= 0:
            print("Inserted money must be a positive number.\n")
            return
        
        if not self.items:
            print("The vending machine is empty.")
            return

        if item_number < 1 or item_number > len(self.items):
            print("Invalid item number.")
            return
        
        item = self.items[item_number - 1]

        if item.quantity <= 0:
            print(f'{item.name} is out of stock.')
            return

        if money < item.price:
            print(f"Insufficient fonds. {item.name} costs ${item.price:.2f}. Inserted money: ${money:.2f}")
            return

        self.sold += 1
        self.revenue += item.price
        item.quantity -= 1

        change = money - item.price
        print(f"Please collect your {item.name}. Change returned: ${change:.2f}. Thank you for your purchase!")

        if item.quantity == 0:
            print(f"{item.name} is now sold out and removed from the machine.")
            self.items.pop(item_number - 1)


# ----------------------------------
vm = VendingMachine()

vm.add_item(Item("Chips", 1.50, 7))
vm.add_item(Item("Chocolate", 2.00, 4))
vm.add_item(Item("Pepsi", 2.50, 5))
vm.add_bulk_items([Item("Candy", 1.00, 1), Item("Juice", 2.50, 2)])


print("\n**** Welcome to the Vending Machine ****\n")
vm.show_items()
print()

vm.buy_item(2, 3.00)
vm.buy_item(1, 1.00)
vm.buy_item(3, 1.00)
vm.buy_item(3, 4.00)
vm.buy_item(4, 5.00)
vm.buy_item(5, 2.00)

print()
vm.show_stats()
print()
vm.show_items()
