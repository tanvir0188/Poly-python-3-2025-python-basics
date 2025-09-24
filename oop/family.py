class Family:
    def __init__(self,my_name,father_name,mother_name,sister_name,brother_name,):
        self.my_name=my_name
        self.father_name=father_name
        self.mother_name=mother_name
        self.sister_name=sister_name
        self.brother_name=brother_name


f1=Family('Awal','A','N','A','R')

print(f'Name : {f1.my_name}\nFather name : {f1.father_name}\nMother name : {f1.mother_name}\nSister name : {f1.sister_name}\nBrother name : {f1.brother_name}')
