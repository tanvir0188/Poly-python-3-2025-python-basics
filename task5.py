# ============================
# Item class
# ============================
class Item:
    def __init__(self, name, price, quantity=1):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Item price must be a positive number.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        self.name = name.strip()
        self.price = float(price)
        self.quantity = quantity

    def __repr__(self):
        return f"Item:(name='{self.name}', price={self.price:.2f}, quantity={self.quantity})"


# ============================
# VendingMachine class
# ============================
class VendingMachine:
    sold = 0
    revenue = 0.0

    def __init__(self):
        self.items = []

    # Add single item
    def add_item(self, item):
        # If same item exists, increase quantity
        for existing_item in self.items:
            if existing_item.name == item.name and existing_item.price == item.price:
                existing_item.quantity += item.quantity
                return
        self.items.append(item)

    # Add multiple items at once
    def add_bulk_items(self, items):
       for item in items:
          self.add_item(item)


    # Buy an item
    def buy_item(self, name, money):
        print(f"✔[DEBUG] You paid: {money} taka")
        # Validate money
        if not isinstance(money, (int, float)) or money <= 0:
            print("Money must be a positive number.🙄")
            return

        if not self.items:
            print("No items available.🙁")
            return

        for i, item in enumerate(self.items):
            if item.name == name:
                if item.quantity <= 0:
                    print(f"{item.name} is out of stock.")
                    return

                if money < item.price:
                    print(f"Not enough money. {item.name} costs {item.price} taka.")
                    return

                # Successful purchase
                item.quantity -= 1
                VendingMachine.sold += 1
                VendingMachine.revenue += item.price
                change = money - item.price
                print(f"💸{item.name} sold! Paid: {money} taka, Price: {item.price} taka, Change: {change} taka")


                # Remove item if quantity reaches 0
                if item.quantity == 0:
                    self.items.pop(i)
                return

        print("This item is not available.⛔")

    # Show machine stats
    def show_stats(self):
        print(f"Total items sold: {VendingMachine.sold}")
        print(f"Total revenue:💲{VendingMachine.revenue:.2f}")

    # Show items with quantity
    def show_items(self):
        if not self.items:
            print("No items in the machine.❌")
            return
        print("Items available👌:")
        for item in self.items:
            print(f" ✔{item.name} ({item.price} taka) x{item.quantity}")


# ============================
# Example usage
# ============================
vm = VendingMachine()

# Add bulk items
vm.add_bulk_items([
    Item("Chips", 30, 3),
    Item("Coke", 50, 2),
    Item("Juice", 40, 1),
    Item('Pepsi',30,2)
])

vm.show_items()
print()

# Buy items
vm.buy_item("Chips", 100)   
vm.buy_item("Juice", 50)   
vm.buy_item("Coke", 25)  
vm.buy_item("Pepsi", 30)
vm.buy_item("ice-cream",50)   

print()
vm.show_items()
print()
vm.show_stats()
print()
