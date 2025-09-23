class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price

class VendingMachine:
  def __init__(self):
    self.items = []

  def add_item(self, item):
    self.items.append(item)

  def show_items(self):
    print("Items available:")
    for i in range(len(self.items)):
      item = self.items[i]
      print(f"{i + 1}. {item.name} - ${item.price:.2f}")

# Usage
vm = VendingMachine()
vm.add_item(Item("Chips", 1.50))
vm.add_item(Item("Soda", 2.00))
vm.show_items()
