
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
    index = 1 
    for item in self.items:
      print(f"{index}. {item.name} - ${item.get_price():.2f}")
      print(f"Packaging: {item.packaging()}")
      print(f"Offer: {item.offer()}")
      index += 1


  def buy_item(self, item_number, money):
    if item_number < 1 or item_number > len(self.items):
      print("Invalid item number.")
      return
    item = self.items[item_number-1]
    if money < item.get_price():
      print("Insufficient funds.")
      return
    self.sold += 1
    self.revenue += item.get_price()
    
    change = money - item.get_price()
    print(f"Dispensing {item.name}. Change: ${change:.2f}")
from items.drink import Drink
from items.snack import Snack
from items.gum import Gum
import random


# example usage
if __name__ == "__main__":
  items = [
    Snack("Chips", 2.50),
    Snack("Chocolate", 1.25),
    Snack("Cookies", 1.75),
    Drink("Soda", 1.75),
    Drink("Water", 1.00),
    Drink("Juice", 2.00),
    Gum("Mint Gum", 0.50),
    Gum("Bubble Gum", 0.75),
    Gum("Chewing Gum", 0.60),
  ]

  # Create vending machine and stock items
  machine = VendingMachine()
  machine.add_bulk_items(items)

  # Show available items
  machine.show_items()


print("Customer 1 buys Chips with $3.00")
machine.buy_item(1, 3.00)

print("\nCustomer 2 buys Soda with $2.00")
machine.buy_item(2, 2.00)

print("\nCustomer 3 buys Gum with $1.00")
machine.buy_item(3, 1.00)

print("\nCustomer 4 buys Water with $0.50 (not enough money)")
machine.buy_item(4, 0.50)

print("\nCustomer 5 buys Chocolate with $2.00")
machine.buy_item(5, 2.00)

print("\n====== Final Stats ======")
machine.show_stats()
