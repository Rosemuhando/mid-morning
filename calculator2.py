from controlstatments import first

first = int (input("enter first number: "))
operator =input("enter operator:")
second = int (input("enter second number:"))
if operator == "+":
    print(first + second)
elif operator == "*":
    print(first * second)
if operator == "/":
    print(first /second)
if operator == "-":
    print(first - second)

