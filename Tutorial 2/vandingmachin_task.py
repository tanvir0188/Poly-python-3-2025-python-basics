#task 1
class Item:
  def __init__(self,name,price,quantity=1):
    #item name valrdition 
    if not isinstance(name,str) or not name.strip():
      return ValueError ('Item name not  non-empaty string ,only string ')
    # item price validition
    if not isinstance(price,(int,float)) or price <= 0:
      return ValueError ("item price not a negitive number, only positive number")
    self.name=name.strip()
    self.price=price
    self.quantity=quantity
class VandingMachine(Item):
  sold=0
  revenue=0
  def __init__(self):
    self.items=[]
    
  def add_item(self,item):
    self.items.append(item)
    
  def add_bulk_item(self,item):
    self.items.extend(item)
   
  def show_status(self):
    print(f"total item sold : {self.item}")
    print(f"total revenue : $ {self.revenue :.2f}") 
  def show_items(self):
    if not self.items:
      print("item is not avilable in the vandingmachine")
      return
    print("item available")
    for i in range(len(self.items)):
      item=self.items[i]
      print(f"{i+1}.{item.name} -$ {item.price} ")
      
      
  #task 2
  def buy_item(self,item_number,money):
    if not self.items:
      print("The vanding machine is empty")
      return
    if not isinstance(money,(int,float)) or money <= 0:
      print("invalid maney inserted",self.money)
      return
    if item_number < 1 or item_number > len(self.items):
      print("invald item number ")
      return
    item=self.items[item_number-1]
    print(f"your selected : {item.name} -$ {item.price} ") 
    if money < item.price:
      print("insufisient found ")
      return
    self.sold += 1
    self.revenue += item.price 
    change=money - item.price
    item.quantity -= 1
    print(f"despensing {item.name} $ {item.price} you pay {money}. change $ : {change}")
    
    if item.quantity <=0:
      print(f"{item.name} is out of stock")
      return
    if item.quantity == 0 :
      self.items.pop(item_number -1)
vm=VandingMachine()
vm.add_item(Item("chips",20,1))
item1=Item("boun",10,2)
item2=Item("bicecut",15,2)
item3=Item("chocklet",5,2)
vm.add_bulk_item([item1,item2,item3])
vm.show_items()
vm.buy_item(2,25)
vm.buy_item(2,25)




#output
# item available
# 1.chips -$ 20 
# 2.boun -$ 10
# 3.bicecut -$ 15
# 4.chocklet -$ 5
# your selected : boun -$ 10
# despensing boun $ 10 you pay 25. change $ : 15
# your selected : boun -$ 10
# despensing boun $ 10 you pay 25. change $ : 15
# boun is out of stock
