from item import Item
class Drink(Item):
    def packaging(self):
        return "Packaged in a bottle."

    def offer(self):
        return "10% off on all drinks."