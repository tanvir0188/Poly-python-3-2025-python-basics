class Item:
  def __init__(self, name, price,quantity):
    
    if name=='':
      raise ValueError('Empty string not a valid item name')
        # print('Empty string not a valid item name')
    if price<0:
      raise ValueError('item price must be a positive integer number')
        # print('Empty string not a valid item name')

    if quantity<0:
      raise ValueError('quantity must be a positive integer number')
        # print('Empty string not a valid item name')
    
    self.name = name
    self.price = price
    self.quantity=quantity

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
      print(f"{i + 1}. {item.name} - ${item.price:.2f} available {item.quantity}")

  def buy_item(self, item_number,quantity, money):
  
    if item_number < 1 or item_number > len(self.items):
      print("Invalid item number.")
      return
    item = self.items[item_number-1]


    if money<0:
      print('money can not bea negative number')
      return
    if quantity>item.quantity:
      print(f"we have {item.quantity} only")
      return
    
    if money < item.price*quantity:
      print("Insufficient funds.")
      return
    self.sold +=quantity
    self.items[item_number-1].quantity-=quantity
    self.revenue += item.price*quantity

    if item.quantity==0:
      self.items.pop(item_number-1)

    change = money - item.price*quantity
    print(f'Dispensing {item.name}. Change: ${change:.2f}')

  

# Usage
vm = VendingMachine()
vm.add_item(Item("a", 10,4))
vm.add_item(Item("Soda", 20,20))
vm.show_items()
vm.buy_item(2,6,50)
vm.show_stats()

item1 = Item("Candy", 30,6)
item2 = Item("Juice", 25,5)
vm.add_bulk_items([item1, item2])

print('-----------------')
vm.show_items()