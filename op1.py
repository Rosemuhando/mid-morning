class person:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def speak(self):
        print(self.name,"is speaking")

person1 = person("mark",24,"teacher")
print(person1.name)
person1.speak()

person2 = person("martha",23,"is an accountant")
print(person2.name)
person2.speak()

