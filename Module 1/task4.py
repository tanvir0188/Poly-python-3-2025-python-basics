#Task 1:
#Create a Family object. It should have attribute such as my_name, father_name, mother_name, sister_name, brother_name
#You have to create the class using a constructor. Initiate it and set values to the attributes.


class Family:

  def __int__(self, my_name, father_name, mother_name, sister_name, brother_name):
      self.my_name=my_name
      self.father_name=father_name
      self.mother_name=mother_name
      self.sister_name=sister_name
      self.brother_name=brother_name

family = Family('habiba', 'matin', 'ripa', 'maisha', 'raiyan')
print(f'family_name:{my.my_name}, family_name:{father.father_name}, family_name:{mother.mother_name}, family_name:{sister.sister_name}, family_name:{brother.brother_name}')

