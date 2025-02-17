# built-in functions/ standard library functions

y = max(67,43,89,90,23)
print("the maximum value is",y)

x = min(15,3,20,78)
print("the minimum value is",x)

# user defined functions
def name():
    print("rose")
name() # calling a function

def product():
    x =10
    y =2
    print(x*y)
product()

# parameter/ variable and arguments/value
def add(a,b):
    print(a+b)
add(1,4)
add(6,7)

def employee(name, gender, position,salary,age):
    print(name,gender,position,salary,age)
employee("rose","female","CEO","560000",56)
employee("john","male","managing director","60000",46)
employee("mary","female","HR","5600000",56)
employee("roan","male","manager","230000",66)
employee("jayne","female","director","900000",26)

# write a program that displays details of 5 students
# use a  user-defined function with the help of a parameter
# and argument
# fullname, age, course, gender


def std(fullname, age, course, gender):
    print(fullname,age,course,gender)
std("joan atieno",26,"cybersecurity","female")
std("prudence agiso",35,"ICT managment","female")
std("donald otieno",34,"software developing","male")
std("dancun opati",40,"education","male")
std("jecinta ayeta",21,"nursing","female")








