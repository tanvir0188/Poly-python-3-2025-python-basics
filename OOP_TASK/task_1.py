class Family:
    def __init__(self, my_name, father_name, mother_name, sister_name, brother_name):
        self.my_name = my_name
        self.father_name = father_name
        self.mother_name = mother_name
        self.sister_name = sister_name
        self.brother_name = brother_name
    
    def show_family(self):
        return f"My name is {self.my_name}. My father's name is {self.father_name}, my mother's name is {self.mother_name}, my sister's name is {self.sister_name}, and my brother's name is {self.brother_name}."
    

family = Family("Nisan", "A", "B", "C", "D")
print(family.show_family())


# print("My name is", family.my_name)
# print("My father's name is", family.father_name)
# print("My mother's name is", family.mother_name)
# print("My sister's name is", family.sister_name)
# print("My brother's name is", family.brother_name)