#  a simple calculator program operators(+,-,*,/)
from secrets import choice

a = int(input("Enter first number: "))

b = int(input("Enter second number: "))


def add(a,b):
    print(a + b)


#subtraction
def sub(a,b):
    print(a - b)


#multiplication
def mul(a, b):
    print(a * b)


#division
def div(a,b):
    print(a / b)



print(1,"add")
print(2,"sub")
print(3,"mul")
print(4,"div")



choice= int(input("enter your choice(1/2/3/4):"))
if  choice == (1/2/3/4) :
    print ("correct choice")
    if choice == 1:
        add(a,b)


    if choice  == 2:
        sub(a,b)


    if choice == 3:
        mul(a,b)

    if  choice  == 4:
        div(a,b)
else:
    print("invalid input",choice)

