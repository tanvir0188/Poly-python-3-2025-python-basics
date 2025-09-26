#Task 1: Validate Item Creation

#Goal: Prevent creating items with invalid data.

#What to do:

#Ensure Item.name is a non-empty string.

#Ensure Item.price is a positive float.

#Task 2: Validate Money in Buy

#Goal: Make the buy_item method more robust.

#What to do:

#Check that the money inserted is a positive number.

#Handle cases where the machine is out of items.

#Task 3: Remove Sold Items

#Goal: Once an item is bought, remove it from the vending machine.


#Task 4: Add Stock Count

#Goal: Keep track of how many units of each item are available.

#What to do:

#Modify Item to have quantity.

#Update add_item and buy_item accordingly.
#For example 
#class Item:
  #def __init__(self, name, price, quantity=1):
    #self.name = name
    #self.price = price
    #self.quantity = quantity

# In buy_item:
#if item.quantity <= 0:
  #print(f"{item.name} is out of stock.")
  #return
#item.quantity -= 1
#if item.quantity == 0:
  #self.items.pop(item_number - 1)



class Item:
  def __init__(self, name, price, quantity=1):
    if not isinstance (name,str):
      print("item name is a non-empty string")
      return
    if not isinstance(price,(int,float)) or price<=0:
      print("Item price is a positive float")
      return
    if not isinstance(quantity,int) or quantity<0:
      print("quantity must be not negative number")
      return
    


    self.name = name
    self.price = price
    self.quantity= quantity
   
class VendingMachine:
  
  def __init__(self):
    self.items = []
    self.sold = 0
    self.revenue = 0


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
      print(f"{i + 1}. {item.name} - ${item.price:.2f} (stock:{item.quantity})")


  def buy_item(self, item_number, money):
    if not isinstance(money,(int,float)) or money<=0:
      print("money inserted is a positive number")
      return
    
    if not self.items:
      print("vending machine is empty")
      return
    
    if item_number < 1 or item_number > len(self.items):
      print("Invalid item number.")
      return
    

    item = self.items[item_number-1]
    if item.quantity<=0:
      print(f'{item.name}is out stock')
      return

    if money < item.price:
      print("Insufficient funds.")
      return
    self.sold +=1
    self.revenue += item.price
    item.quantity -=1 
     
      
    change = money - item.price
    print(f'Dispensing {item.name}. Change: ${change:.2f}')
    
    if item.quantity==0:
      self.items.pop(item_number-1)


      
# Usage
vm = VendingMachine()
vm.add_item(Item("Chips", 1.50, 5))
vm.add_item(Item("Soda", 2.00, 3))
vm.show_items()
vm.buy_item(1, 2.00)
vm.show_stats()

item1 = Item("Candy", 1.00, 2)
item2 = Item("Juice", 2.50, 1)
vm.add_bulk_items([item1, item2])
vm.show_items()
vm.buy_item(4,3)
vm.show_items()


