from abc import ABC, abstractmethod
class Item(ABC):
  def __init__(self, name, price):
    self.name = name
    self.__price = price  # Encapsulation: private attribute

  # Getter and setter for price (controlled access)
  def get_price(self):
    return self.__price
  
  def set_price(self, new_price):
    if new_price > 0:
      self.__price = new_price
    else:
      print("Price must be positive.")

  # Abstract method → must be implemented in child classes
  @abstractmethod
  def packaging(self):
    pass

  # Polymorphism: offer system (default: no offer)
  def offer(self):
    return "No current offers."