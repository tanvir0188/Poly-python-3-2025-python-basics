class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price

class VendingMachine:
  sold = 0
  revenue = 0
  def __init__(self):
    self.items = []

  def add_item(self, item):
    self.items.append(item)
  
  def add_bulk_items(self, items):
    self.items.extend(items)
  
  def show_stats(self):
    print(f"Total items sold: {self.sold}")
    print(f"Total revenue: ${self.revenue:.2f}")

  def show_items(self):
    print("Items available:")
    for i in range(len(self.items)):
      item = self.items[i]
      print(f"{i + 1}. {item.name} - ${item.price:.2f}")

  def buy_item(self, item_number, money):
  
    if item_number < 1 or item_number > len(self.items):
      print("Invalid item number.")
      return
    item = self.items[item_number-1]
    if money < item.price:
      print("Insufficient funds.")
      return
    self.sold +=1
    self.revenue += item.price
      
    change = money - item.price
    print(f'Dispensing {item.name}. Change: ${change:.2f}')

  

# Usage
vm = VendingMachine()
vm.add_item(Item("Chips", 1.50))
vm.add_item(Item("Soda", 2.00))
vm.show_items()
vm.buy_item(1, 2.00)
vm.show_stats()

item1 = Item("Candy", 1.00)
item2 = Item("Juice", 2.50)
vm.add_bulk_items([item1, item2])
vm.show_items()