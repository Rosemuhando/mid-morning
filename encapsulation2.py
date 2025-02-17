class student:
    def __init__(self,name,parent,fee ):
        self.name = name
        self.parent =parent
        self.fee =fee

    def details(self):
        print(self.name,"is the",self.parent)

student1= student("john","peter",45000)
print(student1.name,student1.parent,student1.fee)

student2 = student("jayne","owino",350000)
print(student2.name,student2.parent,student2.fee)

student3 = student("Eunice","mwangi",40000)
print(student3.name,student3.parent,student3.fee)

student4 = student("james","peterson",90000)
print(student4.name,student4.parent,student4.fee)

