#parent/ super/base class

class animal:
    def speak(self):
      print('animal is speaking')

#child class/subclass/derived class
class dog (animal):
   def bark(self):
     print('dog is barking')

class cat (dog):
   def meow(self):
     print('cat is meowing')

a= animal()
d = dog()
d.speak()

c = cat()
c.meow()
