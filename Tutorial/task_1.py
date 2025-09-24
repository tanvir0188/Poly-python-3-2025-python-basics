class Family:
    def __init__(self, my_name, my_age, father_name, father_age, mother_name, mother_age, sister_name, sister_age):
        self.my_name = my_name
        self.my_age = my_age
        self.father_name = father_name
        self.father_age = father_age
        self.mother_name = mother_name
        self.mother_age = mother_age
        self.sister_name = sister_name
        self.sister_age = sister_age


my_family = Family(
    my_name="Jihad", my_age=21,
    father_name="Babbul Hossen", father_age=45,
    mother_name="Rawshanara", mother_age=37,
    sister_name="Banna", sister_age=18
)


print("My name:", my_family.my_name, "Age:", my_family.my_age)
print("Father:", my_family.father_name, "Age:", my_family.father_age)
print("Mother:", my_family.mother_name, "Age:", my_family.mother_age)
print("Sister:", my_family.sister_name, "Age:", my_family.sister_age)
