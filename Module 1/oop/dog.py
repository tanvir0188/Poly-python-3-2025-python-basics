class Dog:
  species = "Canis familiaris"  # Class attribute

  def __init__(self, name, age):
    self.name = name  # Instance attribute
    self.age = age    # Instance attribute

dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.name, dog1.age)  # Buddy 3
print(dog2.name, dog2.age)  # Lucy 5
print(dog1.species)

class Cat:
  species = "Felis catus"  # Class attribute

  def __init__(self):
    self.name = 'gordon'  # Instance attribute
    self.age = 6    # Instance attribute

cat1 = Cat()
print(cat1.name, cat1.age)  # gordon 6
cat1.name = 'tom'
print(cat1.name, cat1.age)  # tom 6