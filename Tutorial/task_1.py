class Item:
    def __init__(self, name, price):
        if not isinstance(name, str) :
            print("Item name must be a non-empty string.")
            return 
        

        if not isinstance(price, (int, float)) or price <= 0:
             print("Item price must be a positive number.")
             return

        self.name = name.strip()
        self.price = float(price)


item1 = Item("cake ", 5.11)  
item2 = Item("Chips", 2.3)
item3 = Item("Chocolate", 2.15)  
print(item1.name, item1.price)
print(item2.name, item2.price)
print(item3.name, item3.price)
