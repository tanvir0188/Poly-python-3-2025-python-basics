class Item:
    def __init__(self,name,price):
        if type(name) != str or name.strip() == "":
           print("Error: Item name must be a non-empty string.")
           return
        if type(price) not in [int,float] or price <= 0:
           print("Errpr: Item price must be a positive number.")
           return
        self.name = name
        self.price = price
item1 = Item("Chips",1.50)
item2 = Item("",2.00)
item3 = Item("soda",-1.00)
item4 = Item("Juice", "2.00")
                