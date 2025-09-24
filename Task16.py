"""
Create a Family object. It should have attribute such as my_name,
father_name, mother_name, sister_name, brother_name

You have to create the class using a constructor.
Initiate it and set values to the attributes
"""


class family:

    def __init__(self,my_name,father_name,mother_name,sister_name,brother_name):
        self.father_name = father_name
        self.mother_name = mother_name
        self.brother_name = brother_name
        self.sister_name = sister_name
        self.my_name = my_name

member = family("Maisha Ferdous","Ferdous Mustafiz","Farhana Akther","Raimin","Sifat")
print(f"father name:{member.father_name},mother name:{member.mother_name},brother name:{member.brother_name},sister name:{member.sister_name}")