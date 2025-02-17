class employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary

    def details(self):
        print(self.name,"is the",self.position )
employee1 = employee("john","CEO",45000)
print(employee1.name,employee1.position,employee1.salary)

employee2 = employee("jayne","managing director",350000)
print(employee2.name,employee2.position,employee2.salary)

employee3 = employee("Eunice","HR",40000)
employee4 = employee("james","CEO",90000)
